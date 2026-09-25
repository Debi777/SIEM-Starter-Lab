# 🛡️ SIEM-in-a-Box: Beginner Cybersecurity Lab

A lightweight, Docker-based Security Information and Event Management (SIEM) home lab designed for practicing log analysis, threat detection, and infrastructure deployment. 

This project simulates a corporate environment where security logs are ingested, parsed, and visualized to detect suspicious activities like brute-force attacks and SQL injections.

## 🏗️ Architecture

This lab is built using **Infrastructure as Code (IaC)** principles and consists of two main components:
1. **The Elastic Stack (ELK):** Runs locally via Docker containers.
   - **Elasticsearch:** The database storing our security events.
   - **Logstash:** The data processing pipeline parsing our custom logs.
   - **Kibana:** The visualization dashboard for threat hunting.
2. **Attack Simulator (`log_generator.py`):** A custom Python script that generates continuous, realistic network traffic mixed with simulated cyber attacks.

## 🚀 Skills Demonstrated
* **Security Monitoring:** Configuring a SIEM to ingest and parse custom data sources.
* **Threat Hunting:** Identifying anomalous behavior (Failed Logins, SQLi) in raw logs.
* **Data Parsing:** Writing Logstash configuration rules to structure JSON logs.
* **DevSecOps:** Utilizing Docker and Docker Compose for rapid, reproducible infrastructure deployment.

## 🛠️ Prerequisites
To run this lab on your own machine, you will need:
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.
* [Python 3.x](https://www.python.org/downloads/) installed.

## 📖 How to Run the Lab

**1. Clone the repository**
```bash
git clone [https://github.com/Debi777/SIEM-Starter-Lab.git](https://github.com/Debi777/SIEM-Starter-Lab.git)
cd SIEM-Starter-Lab
```

**2. Start the simulated attack traffic**
Run the Python script to start generating fake logs. Leave this terminal window open.
```bash
python log_generator.py
```

**3. Launch the SIEM**
Open a second terminal window in the same folder and start the Docker containers.
```bash
docker-compose up -d
```

**4. Access the Dashboard**
* Open your web browser and navigate to `http://localhost:5601` (Kibana).
* Go to **Stack Management > Data Views** and create a new data view matching `siem-lab-logs-*`.
* Navigate to **Discover** to start analyzing the live attack logs!

## 🛑 Cleanup
To stop the SIEM and remove the containers, run:
```bash
docker-compose down
```
