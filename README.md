AI Sentinel – Intelligent CCTV Surveillance System
📌 Overview

AI Sentinel is an AI-powered intelligent CCTV surveillance system developed to automate video monitoring and enhance public safety. The system analyzes uploaded CCTV footage and live camera streams to detect crowd density, suspicious activities, and workplace safety violations. It generates real-time alerts and detailed analysis reports, helping security personnel make faster and more informed decisions.

🚀 Features
🔐 Secure User Authentication (Login & Registration)
🎥 Upload CCTV Videos for Analysis
📹 Add and Manage Live Camera Streams
👥 Crowd Detection and People Counting
🚨 Suspicious Activity Detection
🦺 Workplace Safety Monitoring
📊 Interactive Dashboard with Analytics
🔔 Real-Time Alert Generation
📁 Analysis History and Reports
⚙️ User Settings and Notification Management
🛠️ Technologies Used
Frontend
HTML5
CSS3
JavaScript
Bootstrap
Chart.js
Backend
Python
FastAPI
Uvicorn
Artificial Intelligence
Google Gemini API
OpenCV
FFmpeg
Database
SQLite
Development Tools
Visual Studio Code
Git
GitHub


⚙️ Installation
1. Clone the Repository

cd ai-sentinel
2. Create a Virtual Environment

Windows

python -m venv venv

Activate

venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Install FFmpeg

Download FFmpeg from:

https://ffmpeg.org/download.html

Add the bin folder to your system PATH.

5. Configure Environment Variables

Create a .env file inside the backend folder.

GEMINI_API_KEY=YOUR_GEMINI_API_KEY
PORT=8000
6. Run the Backend
uvicorn backend.main:app --reload

Backend URL

http://127.0.0.1:8000
7. Open the Frontend

Open

frontend/index.html

or serve it using VS Code Live Server.

📊 Modules
Authentication
User Registration
Secure Login
Session Management
Dashboard
Live Statistics
AI Detection Summary
Camera Status
Video Analysis
Upload CCTV Videos
AI-Based Frame Analysis
Crowd Monitoring
Camera Management
Add IP Cameras
Live Camera Monitoring
Camera Status Tracking
Alerts
Suspicious Activity Alerts
Crowd Density Alerts
Workplace Safety Alerts
Reports
Analysis History
Alert Reports
Detection Results
🧠 AI Workflow
User uploads a CCTV video.
FFmpeg extracts representative frames.
Gemini AI analyzes each frame.
Crowd density, suspicious activities, and safety conditions are identified.
Alerts and summaries are generated.
Results are stored in SQLite.
Dashboard displays analytics and reports.
📡 API Endpoints
Method	Endpoint	Description
POST	/api/auth/register	Register User
POST	/api/auth/login	User Login
POST	/api/upload-video	Upload Video
POST	/api/analysis/start	Start AI Analysis
GET	/api/analysis/results/{id}	View Results
GET	/api/alerts	Fetch Alerts
POST	/api/cameras	Add Camera
📸 Screenshots

Add screenshots here.

Login Page
Dashboard
Upload Video
AI Detection
Alerts
Reports
🎯 Future Enhancements
Live CCTV Streaming Analysis
YOLO-Based Local Object Detection
Face Recognition
Multi-Camera Monitoring
Email & SMS Notifications
Cloud Deployment
Heatmap Generation
Mobile Application Support
👨‍💻 Author

Mahesh Reddy

B.Tech – Computer Science and Engineering

📄 License

This project is developed for educational and academic purposes as part of a B.Tech Mini Project.

⭐ Acknowledgements
Google Gemini API
FastAPI
OpenCV
FFmpeg
SQLite
Bootstrap
Python Community
Open Source Contributors
