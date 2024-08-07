from pytubefix import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip
import os


def video_downloader(link, path, resolution):
    try:
        yt = YouTube(link)

        # Download video
        video_stream = yt.streams.filter(res=resolution).first()
        video_path = os.path.join(path, f"{yt.title}")
        video_stream.download(output_path=path, filename=f"{yt.title}")

        # Download audio
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_path = os.path.join(path, f"{yt.title}_audio.mp4")
        audio_stream.download(output_path=path, filename=f"{yt.title}")

        # Merge video and audio
        merge(video_path, audio_path, os.path.join(path, f"{yt.title}"))

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
