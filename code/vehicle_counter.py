from ultralytics import YOLO

model = YOLO(r'C:\Users\ARUN\Desktop\ATN\yolo11l.pt')

desired_classes = ['motorcycle', 'bus', 'car', 'truck', 'bicycle']
results = model(r'C:\Users\ARUN\Desktop\ATN\dataset\traffic_stock (2).mp4')  


print("HHEELLOO", result, "HHEELLOO")
