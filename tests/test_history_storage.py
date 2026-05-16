import os
from storage.history_storage import HistoryStorage


def test_add_download():
    test_file = "data/test_history.json"

    storage = HistoryStorage(file_path=test_file)
    storage.add_download(
        user_id=123,
        url="https://www.tiktok.com/test",
        file_path="downloads/test.mp4"
    )

    history = storage.get_history(123)

    assert len(history) == 1
    assert history[0]["url"] == "https://www.tiktok.com/test"
    assert history[0]["file_path"] == "downloads/test.mp4"

    if os.path.exists(test_file):
        os.remove(test_file)


def test_clear_history():
    test_file = "data/test_history.json"

    storage = HistoryStorage(file_path=test_file)
    storage.add_download(
        user_id=123,
        url="https://www.tiktok.com/test",
        file_path="downloads/test.mp4"
    )

    storage.clear_history(123)
    history = storage.get_history(123)

    assert history == []

    if os.path.exists(test_file):
        os.remove(test_file)