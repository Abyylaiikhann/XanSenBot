import os
import requests
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

    def resolve_short_url(self, url):
        try:
            if "vt.tiktok.com" not in url and "vm.tiktok.com" not in url:
                return url

            headers = {
                "User-Agent": (
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/120.0.0.0 Safari/537.36"
                )
            }

            response = requests.get(
                url,
                headers=headers,
                allow_redirects=True,
                timeout=30
            )

            return response.url

        except Exception as error:
            raise DownloadError(f"Could not resolve short TikTok link: {error}")

    def download(self, url):
        try:
            final_url = self.resolve_short_url(url)

            output_template = os.path.join(
                self.download_folder,
                "%(id)s.%(ext)s"
            )

            options = {
                "outtmpl": output_template,
                "format": "best[ext=mp4]/best",
                "quiet": False,
                "noplaylist": True,
                "restrictfilenames": True,
                "socket_timeout": 90,
                "retries": 10,
                "fragment_retries": 10,
                "nocheckcertificate": True,
                "cookiesfrombrowser": ("chrome",),
                "http_headers": {
                    "User-Agent": (
                        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/120.0.0.0 Safari/537.36"
                    ),
                    "Referer": "https://www.tiktok.com/"
                }
            }

            with yt_dlp.YoutubeDL(options) as ydl:
                info = ydl.extract_info(final_url, download=True)
                file_path = ydl.prepare_filename(info)

            if not os.path.exists(file_path):
                raise DownloadError("Downloaded file was not found.")

            return file_path

        except DownloadError:
            raise

        except Exception as error:
            raise DownloadError(str(error))