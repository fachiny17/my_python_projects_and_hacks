# This is a simple python script that helps you to screen record in your PC

import cv2
import numpy as np
import mss
import keyboard

file_name = input(
    "Enter the filename(no spaces, only alphabets and hyphene): ")


def start_screen_recording(output_file=f"{file_name}.avi", fps=20):
    """
    Function to start screen recording and save the video.
    Press 'q' to stop recording.
    """
    with mss.mss() as sct:
        # Get screen dimensions
        monitor = sct.monitors[1]
        width, height = monitor["width"], monitor["height"]

        # Set up the VideoWriter to save the recording
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

        print("Recording started. Press 'q' to stop.")
        try:
            while True:
                # Capture the screen
                frame = np.array(sct.grab(monitor))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

                # Write the captured frame to the video file
                out.write(frame)

                # Check if 'q' is pressed to stop recording
                if keyboard.is_pressed("q"):
                    print("Recording stopped.")
                    break
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # Release the VideoWriter
            out.release()


# Run the screen recorder
if __name__ == "__main__":
    print("Press 's' to start recording.")
    while True:
        # Wait for the user to press 's' to start recording
        if keyboard.is_pressed("s"):
            start_screen_recording()
            break
