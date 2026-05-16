import os
import yt_dlp


class DownloadError(Exception):
    pass


class BaseDownloader:
    def download(self, url):
        raise NotImplementedError("Subclasses must implement this method")


class TikTokDownloader(BaseDownloader):
    def __init__(self, download_folder="downloads"):
        self.download_folder = download_folder

        if not os.path.exists(self.download_folder):
            os.makedirs(self.download_folder)

    def download(self, url):
        try:
            output_template = os.path.join(
                self.download_folder,
                "%(title).50s_%(id)s.%(ext)s"
            )

            options = {
                "outtmpl": output_template,
                "format": "mp4/best",
                "quiet": True,
                "noplaylist": True,
            }

            with yt_dlp.YoutubeDL(options) as ydl:
                info = ydl.extract_info(url, download=True)
                file_path = ydl.prepare_filename(info)

            return file_path

        except Exception as error:
            raise DownloadError(f"Failed to download video: {error}")