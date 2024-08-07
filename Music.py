from pytubefix import YouTube


def music_downloader(link, path):
    yt = YouTube(link)
    try:
        audio = yt.streams.filter(only_audio=True).first()
        audio.download(path)
    except Exception as e:
        print(f"ERROR: {e}")
    print("Music successfully downloaded!")
