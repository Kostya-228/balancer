import subprocess
import threading


def start(i):
    subprocess.call(['python', 'media_app.py', f'800{i}'])


for i in range(0, 10):
    t = threading.Thread(target=start, args=(i,))
    t.start()

