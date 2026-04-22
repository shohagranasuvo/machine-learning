from ultralytics import YOLO

model = YOLO("runs/detect/train-2/weights/best.pt")

model.predict(
    source=0,     # webcam
    show=True,
    conf=0.4
)