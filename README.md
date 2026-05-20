# AI-Based Restricted Area Surveillance System

An AI-powered real-time surveillance system built using Python, OpenCV, YOLOv8, and Telegram Bot integration.  
This project detects people entering a restricted area through live video/webcam feed and sends instant Telegram alerts during restricted hours.

---

## Features

- Real-time person detection using YOLOv8
- Restricted area monitoring
- Telegram alert notifications
- Live webcam/video feed support
- Bounding box visualization
- Automatic alert system after specified time
- Lightweight and fast detection model

---

## Technologies Used

- Python
- OpenCV
- YOLOv8 (Ultralytics)
- PyTorch
- Telegram Bot API

---

## Project Workflow

1. Capture live video feed from webcam or CCTV.
2. Detect objects using YOLOv8.
3. Identify persons in the frame.
4. Check whether the person enters the restricted area.
5. Trigger Telegram alert if detection happens after alert time.
6. Display live monitored video feed.

---

## Folder Structure

```bash
project/
│
├── main.py
├── requirements.txt
└── README.md

Installation
1. Clone the Repository
git clone <your-repository-link>
cd project-name
2. Install Dependencies
pip install -r requirements.txt

Or install manually:

pip install ultralytics opencv-python torch pyTelegramBotAPI
Download YOLOv8 Model

The project uses the YOLOv8 Nano model.

model = YOLO('yolov8n.pt')

It downloads automatically during first execution if not available.

Telegram Bot Setup
Step 1: Create Telegram Bot
Open Telegram
Search for @BotFather
Create a new bot
Copy the BOT TOKEN
Step 2: Get Chat ID
Create a Telegram group or use personal chat
Add the bot to the group
Get the Chat ID

Update these values in the code:

BOT_TOKEN = 'YOUR_BOT_TOKEN'
CHAT_ID = 'YOUR_CHAT_ID'
Restricted Area Setup

Define the restricted area coordinates:

RESTRICTED_AREA = [(100, 100), (500, 400)]
First point → Top-left corner
Second point → Bottom-right corner
Alert Time Configuration

Set the alert trigger time:

ALERT_TIME = 22

Example:

22 = 10 PM
Alerts trigger only after 10 PM
Run the Project
python main.py

Press Q to quit the application.

Output
Green rectangle → Restricted area
Red rectangle → Person detected inside restricted area
Telegram alert sent when detection occurs during restricted hours
Sample Alert
Person detected in restricted area at 23:15:10
