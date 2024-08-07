from Music import music_downloader
from Video import video_downloader


if __name__ == '__main__':
    while True:
        choice = input("Would you like to download a VIDEO or MUSIC? (1/2)\n")
        if choice == '1':
            url = input("Enter YouTube Link: ")
            url_path = input("Enter Path: ")
            quality = input("Enter Resolution: ")
            video_downloader(url, url_path, quality)
            break
        elif choice == '2':
            url = input("Enter YouTube Link: ")
            url_path = input("Enter Path: ")
            music_downloader(url, url_path)
            break
        elif choice != '1' and choice != '2':
            print("Invalid input, please choose either 1 or 2.")
