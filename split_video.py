import cv2
import os

# Function to extract frames
def FrameCapture(path, output_dir="splited_images", frame_interval=1):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Path to video file
    vidObj = cv2.VideoCapture(path)

    # Get frames per second (fps)
    fps = int(vidObj.get(cv2.CAP_PROP_FPS))
    interval_frames = frame_interval * fps  # Number of frames to skip for 1 second intervals

    # Used as counter variable
    count = 0
    frame_id = 0

    # Checks whether frames were extracted
    success = True

    while success:
        success, image = vidObj.read()

        # Save the frame at each interval
        if success and count % interval_frames == 0:
            cv2.imwrite(os.path.join(output_dir, "frame%d.jpg" % frame_id), image)
            frame_id += 1

        count += 1

    # Release the video capture object
    vidObj.release()


# Driver Code
if __name__ == '__main__':
    # Calling the function to extract frames every 1 second
    FrameCapture("data/VID_20240908_115227.mp4")
