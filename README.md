# moving_object_detect
A real-time moving object detection system using OpenCV. Captures full-screen frames of moving objects, stores each object's images in separate folders, and converts them into videos. Useful for motion tracking, surveillance, and object behavior analysis.
oving Object Detection using OpenCV

⚙️ Features

Real-time moving object detection using webcam

Automatic folder creation for each detected object

Captures image sequences of tracked objects

Converts captured images into a video

Works efficiently on standard webcams

🧠 Technologies Used

Python

OpenCV

NumPy

OS & Datetime modules

🚀 How It Works

Run the detection script (object_detection.py) to start the webcam.

Moving objects are detected and saved in separate folders.

Run the video creation script (images_to_video.py) to generate a video for each object.

📁 Output Structure
captured_objects/
│
├── object_1_YYYYMMDD_HHMMSS/
│   ├── frame_1.jpg
│   ├── frame_2.jpg
│   └── ...
│
├── object_2_YYYYMMDD_HHMMSS/
│   └── ...

🎥 Example Output

Images: Captured in per-object folders

Video: output_video.avi generated from captured frames
