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


# A script to download YouTube videos using yt-dlp.

# import yt_dlp
#
#
# def download_video(url: str):
#    """Downloads a YouTube video given its URL."""
#    ydl_opts = {
#        # Save file as video title with proper extension
#        'outtmpl': '%(title)s.%(ext)s',
#        'format': 'bestvideo+bestaudio/best',  # Get best quality video and audio
#    }
#    try:
#        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#            ydl.download([url])
#        print("Video downloaded successfully!")
#    except Exception as e:
#        print(f"An error occurred: {e}")
#
#
# if __name__ == "__main__":
#    # Input video URL
#    url = input("Enter video URL: ").strip()
#    if url:
#        download_video(url)
#    else:
#        print("No URL entered. Exiting...")
#
