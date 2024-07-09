from pytube import YouTube
from pytube.exceptions import AgeRestrictedError

def download_video(url):
    try:
        yt = YouTube(url)
        yt.streams.first().download() 
        print(f"Downloaded: {yt.title}")
    except AgeRestrictedError:
        print(f"The video {url} is age restricted and cannot be downloaded without logging in.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = "https://youtu.be/fQWhenQgXo8"
    download_video(url)
