import cv2
import os

# ✅ Use your actual image folder path
image_folder = r'C:\Users\mvsrk\OneDrive\Desktop\obj\captured_objects/object_1_20251031_175455'
output_video = 'output_video.avi'  # output video name (saved in same folder as this script)

# Get all image filenames
images = [img for img in os.listdir(image_folder) if img.endswith(('.png', '.jpg', '.jpeg'))]

# Sort images alphabetically (timestamp-based naming will keep correct order)
images = sorted(images)

if not images:
    print("❌ No images found in the folder!")
    exit()

# Read the first image to get frame dimensions
first_frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = first_frame.shape

# Define video writer (XVID codec, 20 FPS)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter(output_video, fourcc, 20.0, (width, height))

print("[INFO] Creating video from images...")

# Add each image to the video
for image in images:
    frame = cv2.imread(os.path.join(image_folder, image))
    if frame is not None:
        video.write(frame)
    else:
        print(f"[WARNING] Skipped unreadable image: {image}")

video.release()
cv2.destroyAllWindows()

print(f"[✅] Video successfully created: {os.path.abspath(output_video)}")
print("[INFO] All source images are safely kept in the folder.")
