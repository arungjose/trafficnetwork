import cv2
from ultralytics import YOLO
from collections import defaultdict
import time

#Loading the YOLO model
model = YOLO('yolo11n.pt')

"""
class_list

 0: 'person',
 1: 'bicycle',
 2: 'car',
 3: 'motorcycle',
 4: 'airplane',
 5: 'bus',
 6: 'train',
 7: 'truck',
 8: 'boat',
 9: 'traffic light',

 The list continues but for our project we will be focusing on {1, 2, 3, 5, 7}
 only
 
"""
class_list = model.names

# Get the traffic stock video
capture = cv2.VideoCapture('../dataset/traffic_stock (2).mp4')

# Count Line Y-level
line_y = 250

#Dictionary to store object counts by class
class_counts = defaultdict(int)

# Dictionary to keep track of object IDs that have crossed the line
crossed_ids = set()

# Get the starting time when it runs
start_time = time.time()

while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        break

    # Each frame has to be tracked using YOLO
    results = model.track(frame, persist=True, classes = [1, 2, 3, 5, 7])
    #print(results)

    # To ensure that results are not empty
    if results[0].boxes.data is not None:
        # Now get the detected boxe, their class indices, and track IDs
        boxes = results[0]. boxes.xyxy.cpu()
        track_ids = results[0].boxes.id.int().cpu().tolist()
        class_indices = results[0].boxes.cls.int().cpu().tolist()
        confidences = results[0].boxes.conf.cpu()

    # To create a counting mark
    cv2.line(frame, (50, line_y), (700, line_y), (0, 0, 255), 3)

    # Loop through each detected object
    for box, track_id, class_idx, conf in zip(boxes, track_ids, class_indices, confidences):
        
        # Skip objects with confidence less than 0.6
        if conf < 0.6:
            continue
                
        x1, y1, x2, y2 = map(int, box)

        # To find the center of each bounding box
        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2
        cv2.circle(frame, (cx, cy), 4, (49, 245, 49), -1)
        
        class_name = class_list[class_idx]

        cv2.putText(frame, f"Id: {track_id} {class_name}", (x1, y1 - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 17, 255), 2)


        # Check if the object has crossed the line
        if cy > line_y and track_id not in crossed_ids:
            crossed_ids.add(track_id)
            class_counts[class_name] += 1

    # Display the counts on the frame
        y_offset = 30
        for class_name, count in class_counts.items():
            cv2.putText(frame, f"{class_name}: {count}", (50, y_offset),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            y_offset += 30
        
    # Video display
    cv2.imshow("YOLO tracking...", frame)

    # To send the first count after 10secs
    if time.time() - start_time >= 10:
        # Open a file to save the data do far
        f1 = open("lane1.txt", "w")
        # Loop to get every vehicle count
        vehicle_data = {class_name : count for class_name, count in class_counts.items()}
        f1.write(str(vehicle_data))
       
            

    #Key binding to quit --> q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release all resources
capture.release()
cv2.destroyAllWindows()    