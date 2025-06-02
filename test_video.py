from ultralytics import YOLO
import cv2

model = YOLO('best.pt')

video_path = 'match.mp4'
cap = cv2.VideoCapture(video_path)

output_width = 640
output_height = 360

fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # codec
out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (output_width, output_height))

if not cap.isOpened():
    print("Không thể mở video")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    resized_frame = cv2.resize(frame, (output_width, output_height))

    results = model(resized_frame)

    annotated_frame = results[0].plot()

    cv2.imshow('YOLOv8 Detection', annotated_frame)

    out.write(annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
