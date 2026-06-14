from kafka.consumer import build_consumer
from clickhouse import insert_batch
import time

consumer = build_consumer()

BATCH_SIZE = 5000
FLUSH_INTERVAL = 10

buffer = []
last_flush = time.time()

while True:

    records = consumer.poll(timeout_ms=1000)

    for _, messages in records.items():

        for message in messages:
            buffer.append(message.value)

    now = time.time()

    if (
        buffer
        and (
            len(buffer) >= BATCH_SIZE
            or now - last_flush >= FLUSH_INTERVAL
        )
    ):

        insert_batch(buffer)
        consumer.commit()
        buffer.clear()
        last_flush = now
        