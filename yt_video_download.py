# Simple script to download YouTube videos using yt-dlp
import yt_dlp

# Ask the user for a YouTube video URL
url = input("Enter the video URL: ").strip()

try:
    # Basic download options
    # Download the best quality video available
    ydl_options = {'format': 'best'}

    # Options to include subtitles
    # ydl_options = {
    #     'format': 'best',                # Download the best quality video
    #     'writesubtitles': True,          # Download subtitles if available
    #     'subtitleslangs': ['en'],        # Preferred subtitle language (e.g., 'en' for English)
    #     'subtitlesformat': 'srt',        # Subtitle format (e.g., 'srt' or 'vtt')
    #     'outtmpl': '%(title)s.%(ext)s'   # Save video with its title as the filename
    # }

    # Create a downloader object and download the video
    with yt_dlp.YoutubeDL(ydl_options) as downloader:
        downloader.download([url])

    print("Video downloaded successfully!")
except Exception as e:
    print("An error occurred while downloading the video:", e)
