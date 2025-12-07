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


