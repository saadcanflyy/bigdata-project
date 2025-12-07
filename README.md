# 🌐 Big Data Real-Time Pipeline  
### Kafka • Python • Cassandra • Elasticsearch • Kibana

Ce projet met en place une architecture Big Data traitant des données de capteurs IoT en temps réel.  
Il illustre un pipeline complet allant de la production d’événements jusqu’à la visualisation dynamique dans Kibana.

---

## 🚀 **Architecture du projet**

Le pipeline se compose de :

1. **Kafka** – Réception et diffusion des événements IoT  
2. **Python Producer** – Génération de données de capteurs (IoT)  
3. **Python Consumer**  
   - Stockage dans **Cassandra**  
   - Indexation dans **Elasticsearch**
4. **Cassandra** – Base de données NoSQL optimisée pour l’écriture rapide  
5. **Elasticsearch** – Moteur d’analyse temps réel  
6. **Kibana** – Tableau de bord et visualisation en direct des données

---

## 📦 **Technologies utilisées**

| Technologie       | Rôle |
|------------------|------|
| **Docker & Docker Compose** | Orchestration des services |
| **Kafka** | Broker de messages |
| **Cassandra** | Stockage NoSQL distribué |
| **Python** | Producer & Consumer |
| **Elasticsearch 8.x** | Indexation & recherche |
| **Kibana** | Dashboards en temps réel |

---

## 🗂 **Structure du projet**

bigdata-project/
│── docker-compose.yml
│── producer.py
│── consumer_elastic.py
│── README.md

---

## ▶️ Démarrer le projet

### 1️⃣ Lancer les services Docker

```bash
docker compose up -d
Vérifier que tout tourne :

bash
Copier le code
docker compose ps
2️⃣ Lancer le producer Kafka (génération de données IoT)
bash
Copier le code
python producer.py
3️⃣ Lancer le consumer (Cassandra + Elasticsearch)
bash
Copier le code
python consumer_elastic.py
📊 Visualisation Kibana
Accéder à Kibana :

👉 http://localhost:5601

Créer un index pattern :

kotlin
Copier le code
iot-data
Vous pouvez maintenant visualiser :
. Température
. Humidité
. Pression
. Distribution par capteur
. Évolution dans le temps

📁 Kafka : Création du topic
bash
Copier le code
docker compose exec kafka bash

kafka-topics --create \
  --topic iot-sensor \
  --bootstrap-server localhost:9092 \
  --replication-factor 1 \
  --partitions 1
🔄 Redémarrer le projet après extinction du PC
Exécuter simplement :

bash
Copier le code
docker compose up -d
python consumer_elastic.py
python producer.py


🧑‍💻 Auteur

Saad – Étudiant en Big Data (5ᵉ année)
📫 saadcanflyy
🧵 GitHub : https://github.com/saadcanflyy
