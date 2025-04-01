import cv2
from ultralytics import YOLO
from collections import defaultdict
import time

# Load models
general_model = YOLO('yolo11n.pt')  # Using your specified model
ambulance_model = YOLO('my_model.pt')

# Video capture with optimized backend
cap = cv2.VideoCapture('test1.mp4', cv2.CAP_FFMPEG)
if not cap.isOpened():
    print("Error opening video file")
    exit()

# Video timing (15% slower than normal)
original_fps = cap.get(cv2.CAP_PROP_FPS)
WAIT_TIME = int(1150 / original_fps) if original_fps > 0 else 29  # 15% slower than normal

# Configuration
LINE_Y = 250
LANE_DIVIDER_X = 400 
AMBU_BOX_THRESH = 0.3
AMBU_ALERT_THRESH = 0.7

# Tracking variables
vehicle_counts = defaultdict(int)
crossed_ids = set()
ambulance_alert_time = 0

print(f"Running at {1000/WAIT_TIME:.1f} FPS (slightly slower than normal)")
print("Starting left lane traffic counting... Press Q to quit")

while cap.isOpened():
    start_time = time.time()
    ret, frame = cap.read()
    if not ret:
        break
    
    # Run detections with half-precision inference for speed
    vehicle_results = general_model.track(frame, persist=True, classes=[2, 3, 5, 7], half=True)  # FP16
    ambulance_results = ambulance_model.track(frame, persist=True, half=True)
    
    # Draw left lane counting line
    cv2.line(frame, (0, LINE_Y), (LANE_DIVIDER_X, LINE_Y), (0, 0, 255), 3)

    # Process detections
    current_ambulance_detected = False
    
    # Combined processing for efficiency
    for results, is_ambulance in [(ambulance_results, True), (vehicle_results, False)]:
        if results[0].boxes.id is None:
            continue
            
        for box, track_id, *extra in zip(results[0].boxes.xyxy.cpu().numpy(),
                                       results[0].boxes.id.int().cpu().tolist(),
                                       *([results[0].boxes.conf.cpu().numpy()] if is_ambulance else []),
                                       *([results[0].boxes.cls.int().cpu().numpy()] if not is_ambulance else [])):
            x1, y1, x2, y2 = map(int, box)
            cx = (x1 + x2) // 2
            
            # Skip right lane vehicles
            if cx >= LANE_DIVIDER_X:
                continue
                
            if is_ambulance:
                conf = extra[0]
                if conf < AMBU_BOX_THRESH:
                    continue
                    
                color = (0, 255, 0)
                label = "ambulance"
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, f"{track_id}: {label}", (x1, y1-10), 
                          cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
                
                if conf >= AMBU_ALERT_THRESH:
                    current_ambulance_detected = True
                    ambulance_alert_time = time.time()
            else:
                class_id = extra[0]
                class_name = general_model.names[class_id]
                color = (0, 0, 255)
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, f"{track_id}: {class_name}", (x1, y1-10), 
                          cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
                
                # Count crossing
                cy = (y1 + y2) // 2
                if (LINE_Y - 5) <= cy <= (LINE_Y + 5) and track_id not in crossed_ids:
                    crossed_ids.add(track_id)
                    vehicle_counts[class_name] += 1
            
            # Draw center point
            cv2.circle(frame, (cx, (y1+y2)//2), 4, (0, 255, 0), -1)

    # Display
    if current_ambulance_detected or (time.time() - ambulance_alert_time < 5):
        cv2.putText(frame, "AMBULANCE DETECTED!", (frame.shape[1]//2 - 120, 50), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)  # Thinner text for speed

    count_y = 30
    for vehicle_type in ["car", "truck", "bus"]:
        if count := vehicle_counts.get(vehicle_type, 0):
            cv2.putText(frame, f"{vehicle_type}: {count}", (20, count_y),
                      cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            count_y += 30

    cv2.imshow("Left Lane Traffic Counting", frame)
    
    # Adaptive wait time for consistent playback
    elapsed = (time.time() - start_time) * 1000
    remaining_wait = max(1, int(WAIT_TIME - elapsed))
    if cv2.waitKey(remaining_wait) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()