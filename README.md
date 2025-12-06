# IoT Real-Time Data Pipeline (Kafka + Cassandra + Elasticsearch + Kibana)

This project is a mini big data pipeline built with:

- **Python** (producer & consumer)
- **Kafka** (streaming)
- **Elasticsearch + Kibana** (storage & visualization)
- **Docker Compose** (orchestration)

## Architecture

1. A Python **producer** simulates IoT sensor events and sends them to a Kafka topic `iot-sensor`.
2. A Python **consumer** reads events from Kafka and indexes them into Elasticsearch.
3. Kibana is used to build real-time dashboards on top of the `iot-data` index.

## How to run

```bash
# 1. Start all services
docker compose up -d

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Start the producer (Kafka)
python producer.py

# 4. Start the consumer (Elasticsearch)
python consumer_elastic.py
