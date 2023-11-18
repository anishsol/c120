import cv2
import numpy as np

# Function to track the ball in the video
def track_ball(video_path):
    cap = cv2.VideoCapture(video_path)

    # Create a window to display the video
    cv2.namedWindow("Ball Tracking")

    # Create the tracker
    tracker = cv2.TrackerKCF_create()

    # Read the first frame
    ret, frame = cap.read()

    # Select the region of interest (ROI) for tracking
    bbox = cv2.selectROI("Ball Tracking", frame, False)
    tracker.init(frame, bbox)

    while True:
        # Read a new frame
        ret, frame = cap.read()

        if not ret:
            break

        # Update the tracker
        success, bbox = tracker.update(frame)

        # Draw the tracking rectangle
        if success:
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (0, 255, 0), 2, 1)
        else:
            cv2.putText(frame, "Lost", (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

        # Display the frame
        cv2.imshow("Ball Tracking", frame)

        # Exit the program if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close the window
    cap.release()
    cv2.destroyAllWindows()

# Specify the path to your video file
video_path = 'F:\1aa\coding\python projects\c120'

# Call the track_ball function with the video path
track_ball(video_path)
