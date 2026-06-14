from collectors.netflow import collector_v5
from threading import Thread
from time import sleep

collector_thread = Thread(target=collector_v5, daemon=True, args=(2055, 65535))
collector_thread.start()

while True:
    sleep(10)