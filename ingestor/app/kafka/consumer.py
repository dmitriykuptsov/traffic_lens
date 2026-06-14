import json

from kafka import KafkaConsumer


def build_consumer():

    return KafkaConsumer(
        "flows.raw",

        bootstrap_servers=[
            "kafka:9092"
        ],

        value_deserializer=lambda x:
        json.loads(
            x.decode()
        ),

        auto_offset_reset="earliest",

        enable_auto_commit=True,

        group_id="flow-ingestor"
    )