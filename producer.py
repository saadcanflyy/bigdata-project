import json
import random
import time
from datetime import datetime

from kafka import KafkaProducer

# Configuration du producer Kafka
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def generate_sensor_event():
    """Simule une mesure d'un capteur IoT."""
    return {
        "device_id": f"sensor-{random.randint(1, 5)}",
        "temperature": round(random.uniform(18.0, 32.0), 2),
        "humidity": round(random.uniform(30.0, 80.0), 2),
        "pressure": round(random.uniform(950, 1050), 2),
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

if __name__ == "__main__":
    topic = "iot-sensor"
    print(f"Envoi de données sur le topic Kafka '{topic}' ... [Ctrl+C pour arrêter]")

    try:
        while True:
            event = generate_sensor_event()
            producer.send(topic, value=event)
            producer.flush()

            print("Message envoyé :", event)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nArrêt du producer.")
    finally:
        producer.close()
