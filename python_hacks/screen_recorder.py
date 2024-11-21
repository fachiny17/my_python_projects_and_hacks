import cv2
import numpy as np
import mss
import keyboard
import pyaudio
import wave
import threading

# Get filename from user input
file_name = input(
    "Enter the filename (no spaces, only alphabets and hyphens): ")

# Audio settings
audio_format = pyaudio.paInt16
channels = 1
rate = 44100
chunk_size = 1024
output_audio_file = f"{file_name}.wav"

# Initialize audio stream
p = pyaudio.PyAudio()


def record_audio():
    """
    Function to record audio while screen is being recorded.
    """
    # Open audio stream
    stream = p.open(format=audio_format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk_size)

    print("Recording audio...")
    frames = []

    # Record audio until 'q' is pressed
    while True:
        try:
            # Read audio data from the microphone
            data = stream.read(chunk_size)
            frames.append(data)

            if keyboard.is_pressed('q'):  # Stop when 'q' is pressed
                break
        except Exception as e:
            print(f"Error recording audio: {e}")
            break

    # Stop the audio stream
    stream.stop_stream()
    stream.close()

    # Save audio to a .wav file
    with wave.open(output_audio_file, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(audio_format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))

    print("Audio recording saved.")


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


# Run the screen and audio recorder
if __name__ == "__main__":
    print("Press 's' to start recording.")
    while True:
        # Wait for the user to press 's' to start recording
        if keyboard.is_pressed("s"):
            # Start both the screen recording and audio recording in separate threads
            screen_thread = threading.Thread(target=start_screen_recording)
            audio_thread = threading.Thread(target=record_audio)

            screen_thread.start()
            audio_thread.start()

            # Wait for both threads to finish
            screen_thread.join()
            audio_thread.join()
            break
