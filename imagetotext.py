import cv2
import pytesseract
import pandas as pd
import re

# Set Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\behnoush.garshasebi\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# Load video file
video_path = "input2.mp4"  # Replace with your actual video file
cap = cv2.VideoCapture(video_path)

frame_interval = 10  # Process every 10th frame
frame_count = 0

# Data storage for Excel
data = []

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break  # Stop when the video ends

    if frame_count % frame_interval == 0:
        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply thresholding (removes noise)
        gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        # Denoise with Gaussian Blur
        gray = cv2.GaussianBlur(gray, (3, 3), 0)

        # Use Tesseract OCR with better settings
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(gray, config=custom_config, lang="eng").strip()

        # Extract relevant data (timestamp, speed, GPS)
        time_match = re.search(r"\d{2}:\d{2}:\d{2}", text)  # HH:MM:SS format
        speed_match = re.search(r"\d+\s?MPH", text)  # Speed with MPH
        gps_match = re.search(r"N\d+\.\d+\sW\d+\.\d+", text)  # GPS coordinates (Nxx.xxxx Wxx.xxxx)

        # Assign extracted values
        time_stamp = time_match.group() if time_match else "N/A"
        speed = speed_match.group() if speed_match else "N/A"
        gps_location = gps_match.group() if gps_match else "N/A"

        # Store in data list
        data.append([frame_count, time_stamp, speed, gps_location])

    frame_count += 1

cap.release()
cv2.destroyAllWindows()

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Frame", "Time", "Speed", "GPS Location"])

# Save to Excel
excel_filename = "extracted_video_data.xlsx"
df.to_excel(excel_filename, index=False)

print(f"✅ Data extracted and saved to {excel_filename}")
