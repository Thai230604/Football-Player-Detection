from ultralytics import YOLO

# Load mô hình
model = YOLO('best.pt')

# Predict ảnh
results = model.predict("D:\\FIFA YOLO Project.v1i.yolov8\\test\\images\\var_3_bundesliga_2020_2_frame_4800_jpg.rf.8ba55cf9e99eaf1ac089bcd69f6dca63.jpg", imgsz=640)

# Hiển thị ảnh có kết quả nhận diện
results[0].show()
