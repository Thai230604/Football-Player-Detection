FROM python:3.10-slim

# Cài các thư viện hệ thống cần thiết cho OpenCV
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
 && rm -rf /var/lib/apt/lists/*

# Thiết lập thư mục làm việc
WORKDIR /app

# Copy code vào container
COPY requirements.txt .


# Cài thư viện Python
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .
# Chạy mặc định
CMD ["python", "test_image.py"]
