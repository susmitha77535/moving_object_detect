import cv2
import numpy as np
import datetime
import os

# Base folder for storing all detected objects
base_output_dir = "captured_objects"
if not os.path.exists(base_output_dir):
    os.makedirs(base_output_dir)

# Initialize webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()

# Read initial frames
ret, frame1 = cap.read()
ret, frame2 = cap.read()

object_id = 0
object_trackers = []  # [ (x, y, w, h, folder_path) ]

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 25, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Copy frame for display
    display_frame = frame1.copy()

    # Track current object positions
    current_objects = []

    for contour in contours:
        if cv2.contourArea(contour) < 1200:
            continue

        (x, y, w, h) = cv2.boundingRect(contour)
        current_objects.append((x, y, w, h))
        cv2.rectangle(display_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Match new contours to existing tracked objects
    for (x, y, w, h) in current_objects:
        matched = False
        for i, (ox, oy, ow, oh, folder) in enumerate(object_trackers):
            # Check overlap (intersection over union)
            if (x < ox + ow and x + w > ox and y < oy + oh and y + h > oy):
                object_trackers[i] = (x, y, w, h, folder)
                matched = True
                break

        # If no existing object matches → new object detected
        if not matched:
            object_id += 1
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            folder_name = f"object_{object_id}_{timestamp}"
            folder_path = os.path.join(base_output_dir, folder_name)
            os.makedirs(folder_path)
            print(f"[INFO] New object detected — Folder created: {folder_path}")
            object_trackers.append((x, y, w, h, folder_path))

    # Save frames for tracked objects
    for (x, y, w, h, folder) in object_trackers:
        obj_crop = frame1[y:y + h, x:x + w]
        if obj_crop.size > 0:
            frame_name = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f") + ".jpg"
            cv2.imwrite(os.path.join(folder, frame_name), obj_crop)

    # Display
    cv2.imshow("Multiple Object Tracking & Saving", display_frame)

    # Update frames
    frame1 = frame2
    ret, frame2 = cap.read()
    if not ret:
        break

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
print("[INFO] Program ended.")
