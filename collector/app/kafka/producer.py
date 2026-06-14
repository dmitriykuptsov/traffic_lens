import json
from kafka import KafkaProducer

class FlowProducer:

    def __init__(
        self,
        brokers: list[str],
        topic: str
    ):
        self.topic = topic

        self.producer = KafkaProducer(
            bootstrap_servers=brokers,
            value_serializer=lambda x: json.dumps(x).encode()
        )

    def publish(self, flow: dict):

        self.producer.send(
            self.topic,
            flow
        )

    def flush(self):

        self.producer.flush()
