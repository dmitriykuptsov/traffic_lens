from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=[
        "kafka:9092"
    ]
)

def send(json_bytes):
    """Sends the flow record to Kafka"""
    producer.send(
        "flows.raw",
        json_bytes
    )