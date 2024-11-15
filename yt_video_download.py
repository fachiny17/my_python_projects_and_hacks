# Simple script to download YouTube videos using yt-dlp
import yt_dlp

# Ask the user for a YouTube video URL
url = input("Enter the video URL: ").strip()

try:
    # Basic download options
    # Download the best quality video available
    ydl_options = {'format': 'best'}

    # Create a downloader object and download the video
    with yt_dlp.YoutubeDL(ydl_options) as downloader:
        downloader.download([url])

    print("Video downloaded successfully!")
except Exception as e:
    print("An error occurred while downloading the video:", e)
