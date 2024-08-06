from pytubefix import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip
import os


def download(link, path, resolution):
    try:
        yt = YouTube(link)

        video_stream = yt.streams.filter(res=resolution).first()
        video_path = os.path.join(path, "video.mp4")
        video_stream.download(output_path=path, filename="video.mp4")

        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_path = os.path.join(path, "audio.mp4")
        audio_stream.download(output_path=path, filename="audio.mp4")

        merge(video_path, audio_path, os.path.join(path, yt.title))

    except Exception as e:
        print(f"ERROR: {e}")


def merge(video_path, audio_path, output_path):
    try:
        video_clip = VideoFileClip(video_path)
        audio_clip = AudioFileClip(audio_path)
        video_with_audio = video_clip.set_audio(audio_clip)

        video_with_audio.write_videofile(output_path, codec="libx264", audio_codec="aac")

        video_clip.close()
        audio_clip.close()
        os.remove(video_path)
        os.remove(audio_path)

    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == '__main__':
    url = input("Enter YouTube Link: ")
    url_path = input("Enter Path: ")
    quality = input("Enter Resolution: ")
    download(url, url_path, quality)
