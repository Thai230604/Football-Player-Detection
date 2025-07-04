# ⚽ Football Object Detection with YOLOv8

This project applies **YOLOv8** object detection to detect players, referees, and other objects in football match videos. The model was trained using the Ultralytics YOLO framework and deployed to analyze both images and videos.

## 🚀 Demo kết quả

![Demo](./demo/output.gif)

![Demo](./demo/image_test.png)

---
## Link Dataset

https://drive.google.com/drive/folders/1c6hijyPA4dP8c6nEKCUQgNtoLfWxzryA?usp=sharing

## 📂 Project Structure
```bash
FOOTBALL/
│
├── demo # include demo image and demo gif 
├── best.pt # Trained YOLOv8 model weights
├── match.mp4 # Original input football video
├── test_image.py # Script to run inference on a single image
├── test_video.py # Script to run inference on video
├── train.ipynb # Training notebook using Ultralytics YOLOv8
└── README.md # Project documentation

```
---

## 🚀 How to Run

### 1. Clone this repository

```bash
git clone https://github.com/your-username/football-yolov8.git

```
### 2. Install dependencie
Make sure you have Python 3.8+ installed.
```bash
pip install ultralytics opencv-python
```
### 3. Run Detection
🔍 Detect on Image
```bash
python test_image.py
```
🎥 Detect on Video
```bash
python test_video.py
```

🧠 Model
The model used is YOLOv8 trained with a custom football dataset labeled using Roboflow.
```bash
Model file: best.pt

Framework: Ultralytics YOLOv8
```
📦 Output
```bash
The output video will be saved as output.mp4 with bounding boxes and labels drawn on each frame.
```

📬 Contact
If you have any questions or feedback, feel free to contact me.
```bash
👤 Your Name  
📧 pthai9120@gmail.com  
```

---