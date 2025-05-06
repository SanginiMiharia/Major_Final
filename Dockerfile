FROM python:3.11-slim

# Install dependencies for Tkinter and OpenCV
RUN apt-get update && \
    apt-get install -y python3-tk libgl1-mesa-glx && \
    rm -rf /var/lib/apt/lists/*

# Set workdir
WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY steganography.py .

# Default command
CMD ["python", "steganography.py"]
