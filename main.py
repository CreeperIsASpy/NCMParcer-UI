import webview
import threading
import time
import sys

from src.backend.main import start_api_server


if __name__ == '__main__':
    t = threading.Thread(target=start_api_server)
    t.daemon = True
    t.start()
    time.sleep(1)

    window = webview.create_window(
        title='网易云音乐工具箱',
        url='http://localhost:5000',
        width=1000,
        height=700
    )

    webview.start()

    sys.exit()
