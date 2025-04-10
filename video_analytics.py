import cv2
import torch
from ultralytics import YOLO
import time
from datetime import datetime
import telebot

# Initialize YOLOv8 model
model = YOLO('yolov8n.pt')

# Telegram bot setup
BOT_TOKEN = '8077055787:AAGIbxRCWqtQwOcYdAEhtUvu0gb6rIRqOQ8'
CHAT_ID = '-4746993338'
bot = telebot.TeleBot(BOT_TOKEN)
# Define the restricted area (rectangle coordinates)
RESTRICTED_AREA = [(100, 100), (500, 400)]  # Top-left and bottom-right points
# Set the time after which detections should trigger alerts
ALERT_TIME = 22  # 11 PM

def is_person_in_area(box, area):
    x1, y1, x2, y2 = box
    ax1, ay1 = area[0]
    ax2, ay2 = area[1]
    return (ax1 < x1 < ax2 and ay1 < y1 < ay2) or (ax1 < x2 < ax2 and ay1 < y2 < ay2)


def send_telegram_alert(message):
    try:
        bot.send_message(CHAT_ID, message)
    except Exception as e:
        print(f"Failed to send Telegram alert: {e}")

def process_video(video_source=0):  # 0 for webcam, or provide a video file path
    cap = cv2.VideoCapture(video_source)
    
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        
        # Get current time
        current_time = datetime.now().time()
        
        # Perform YOLOv8 detection
        results = model(frame)
        
        # Draw restricted area
        cv2.rectangle(frame, RESTRICTED_AREA[0], RESTRICTED_AREA[1], (0, 255, 0), 2)
        
        # Process detections
        for r in results:
            boxes = r.boxes
            for box in boxes:
                if box.cls == 0:  # Class 0 is typically 'person' in COCO dataset
                    x1, y1, x2, y2 = box.xyxy[0].tolist()
                    if is_person_in_area((x1, y1, x2, y2), RESTRICTED_AREA):
                        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
                        if current_time.hour >= ALERT_TIME:
                            alert_message = f"Person detected in restricted area at {current_time.strftime('%H:%M:%S')}"
                            send_telegram_alert(alert_message)
        
        # Display the frame
        cv2.imshow('Video Analytics', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Run the video processing
process_video()

        
