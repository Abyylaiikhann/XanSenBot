import json
import os
from datetime import datetime


class HistoryStorage:
    def __init__(self, file_path="data/history.json"):
        self.file_path = file_path

        if not os.path.exists("data"):
            os.makedirs("data")

        if not os.path.exists(self.file_path):
            self.save_data({})

    def load_data(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)

        except json.JSONDecodeError:
            return {}

        except FileNotFoundError:
            return {}

    def save_data(self, data):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def add_download(self, user_id, url, file_path):
        data = self.load_data()

        user_id = str(user_id)

        if user_id not in data:
            data[user_id] = []

        download_record = {
            "url": url,
            "file_path": file_path,
            "downloaded_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        data[user_id].append(download_record)

        self.save_data(data)

    def get_history(self, user_id):
        data = self.load_data()
        user_id = str(user_id)

        return data.get(user_id, [])

    def clear_history(self, user_id):
        data = self.load_data()
        user_id = str(user_id)

        if user_id in data:
            data[user_id] = []

        self.save_data(data)