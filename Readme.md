☁️ AWS Security + Attendance Dashboard
📍 IoT-Based Smart Attendance System with Security Monitoring
🚀 Project Overview

This project is a real-time smart attendance system that uses GPS (IoT concept), AWS Cloud services, and OTP verification to securely mark student attendance.

It ensures that:

✅ Students can login only from the authorized classroom location
✅ Access is allowed only within class timings
✅ OTP verification ensures secure authentication
✅ All login activities are logged and monitored using AWS S3
🌐 What is IoT in this Project?

IoT (Internet of Things) refers to connecting real-world devices (like mobile phones) to the internet to collect and use data.

👉 In this project:

The student's device (browser/mobile) acts as an IoT device
It sends real-time GPS location (latitude & longitude)
The system verifies whether the student is inside the classroom

✔ This makes the system real-world, smart, and secure

🧠 Features
🔐 1. Smart Login System
User ID + Password authentication
Location-based validation (GPS)
Time-based restriction (class hours)
📍 2. Auto Location Detection (IoT)
Automatically detects student location using browser GPS
No manual entry required
🔑 3. OTP Verification
OTP sent via AWS SNS
Ensures secure login
🛡 4. Security Monitoring (S3 Logs)
Every login is stored in AWS S3
Logs include:
user_id
login status
timestamp
📊 5. Dashboard Analytics
Upload logs (JSON / TXT / LOG)
Displays:
Total Requests
Success
Denied
Detects suspicious activity
🏗️ Architecture
User (Browser GPS)
        ↓
Streamlit Dashboard
        ↓
API Gateway
        ↓
AWS Lambda (Login Logic)
        ↓
DynamoDB (User Data)
        ↓
SNS (OTP Email)
        ↓
S3 (Logs Storage)
⚙️ AWS Services Used
AWS Lambda → Backend logic
API Gateway → API endpoint
DynamoDB → User database
SNS → OTP email system
S3 → Log storage
📦 Dependencies

Install required Python libraries:

pip install streamlit requests streamlit-js-eval boto3
📁 Project Structure
project/
│
├── app.py                 # Streamlit frontend
├── lambda_function.py     # AWS Lambda code
├── README.md
🛠️ Setup Instructions
🔹 Step 1: Create DynamoDB Table
Go to AWS → DynamoDB
Create table:
Table name: Users
Primary key: user_id (String)
Add users with attributes:
user_id
password
latitude
longitude
allowed_radius
start_time
end_time
mfa_enabled
email
🔹 Step 2: Setup SNS (OTP Email)
Go to AWS SNS
Create Topic → s3-alert-topic
Add subscriptions:
Protocol: Email
Enter student email

📌 IMPORTANT:
Confirm subscription via email

🔹 Step 3: Create S3 Bucket
Go to AWS S3
Create bucket:
log-bucket-project-3005
Create folder:
logs/
🔹 Step 4: Deploy Lambda Function
Go to AWS Lambda
Create function
Paste Lambda code
Add permissions:
DynamoDB Full Access
S3 Full Access
SNS Full Access
🔹 Step 5: Setup API Gateway
Create HTTP API
Connect Lambda
Enable POST method
Deploy API

👉 Copy Invoke URL

🔹 Step 6: Update Streamlit Code

Replace:

API_URL = "YOUR_API_URL"

with your API Gateway URL

🔹 Step 7: Run the Application
streamlit run app.py
▶️ How to Use
Open dashboard
Enter:
User ID
Password
Allow location access
Receive OTP
Enter OTP
Login success
📊 S3 Monitoring
Download .json logs from S3
Upload in dashboard
View:
Requests
Success/Denied
Suspicious activity alerts
🖼️ Screenshots
🔐 Login Dashboard

📍 Location Detection

🔑 OTP Verification

📊 S3 Monitoring

🔥 Output Example
{
  "user_id": "101",
  "status": "Access granted",
  "timestamp": "2026-04-06"
}
🚨 Suspicious Activity Detection
If denied requests detected → Alert shown
Helps identify unauthorized access
🎯 Advantages
Prevents proxy attendance
Ensures real-time tracking
Secure and scalable
Cloud-based architecture
🚀 Future Enhancements
Live dashboard (auto fetch S3 logs)
Graph analytics
Face recognition
Mobile app integration
👨‍💻 Author
Avni
📌 Conclusion

This project demonstrates a real-world IoT + Cloud-based solution for secure attendance and monitoring, combining:

Location intelligence
Authentication
Cloud logging
Security analytics
