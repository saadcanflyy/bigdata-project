from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json

es = Elasticsearch(
    hosts=["http://localhost:9200"],
    verify_certs=False
)

if not es.ping():
    print("❌ Impossible de se connecter à Elasticsearch.")
else:
    print("✅ Connecté à Elasticsearch.")

consumer = KafkaConsumer(
    "iot-sensor",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    auto_offset_reset="earliest",
    enable_auto_commit=True,
)

print("📥 Lecture des messages Kafka... [Ctrl+C pour arrêter]")

for message in consumer:
    event = message.value
    print("📌 Reçu :", event)

    es.index(
        index="iot-data",
        document=event
    )
    print("✓ Indexé dans Elasticsearch")
