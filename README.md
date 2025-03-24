# EASY Imagetotext---Nextbase-Camera-Videos
This project extracts textual information from a video using Python, OpenCV, and Tesseract OCR. It processes frames from a video to detect and extract timestamps, speed, and GPS coordinates using OCR and saves the extracted data into an Excel file.

TUTORIAL:

Notes:
one nextbase camera videos are shortened and also put in here as optional inputs and the 2 outputs to check with your own.
 This code extracts text from every 10th frame: means the code does not analyze every single frame in the video,  it skips 9 frames and only processes the 10th one. Which is faster and often enough for extracting changing information like speed, time, or GPS.
But, the frame interval is customizable to control processing frequency.
1. Install Tesseract OCR
Tesseract is the OCR engine your script uses to read text from images.
Download:
Windows installer:
 https://github.com/UB-Mannheim/tesseract/wiki\
Download the file named something like: Tesseract-OCR setup for Windows 64-bit (e.g., tesseract-ocr-w64-setup-v5.3.0.20221222.exe)
Install it in this path: C:\Program Files\Tesseract-OCR\
2. Set Tesseract Path in Your Python Code
In the code, this line sets Tesseract path:
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
3. Install Python Packages
Open command/ Terminal:
pip install opencv-python pytesseract pandas openpyxl

4. Place Your Video
Put your video file (e.g., input2.mp4) in the same folder as your Python script, or update the path in this line:
video_path = "input2.mp4"

5. Run the Script:imagetotext.py
It will:
Process the video, Extract text from every 10th frame, Save the output to extracted_video_data.xlsx




