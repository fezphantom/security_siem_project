# 🔐 Security SIEM Project

## 📌 Overview
This project demonstrates the design and implementation of a **Security Information and Event Management (SIEM)** pipeline for monitoring, detecting, and analyzing security events.

The system simulates a **Security Operations Center (SOC)** workflow by ingesting logs, applying detection rules, and generating alerts for suspicious activity such as unauthorized access attempts and anomalies.

---

## 🎯 Objectives

- Build a centralized **log collection and analysis pipeline**
- Detect suspicious activities using **rule-based detection**
- Simulate **SOC alert triage and investigation**
- Visualize security events and trends
- Develop hands-on experience with **SIEM workflows**

---

## 🧠 Skills Demonstrated

- Log analysis and parsing  
- Threat detection and alerting  
- Incident investigation and triage  
- SIEM architecture and workflows  
- Data analysis using Python  
- Dashboarding and visualization  

---

## 🏗️ Architecture
Log Sources → Ingestion → Parsing → Detection → Alerts → Visualization


---

## ⚙️ Technologies Used

- **Programming:** Python  
- **Libraries:** Pandas, Regex, Matplotlib  
- **Environment:** Linux / Local Machine  
- **SIEM Concepts:** Log aggregation, event correlation, alerting  

---

## 📂 Project Structure
security_siem_project/
│── logs/ # Raw log files
│── scripts/ # Parsing and detection scripts
│── data/ # Processed data
│── main.py # Main execution script
│── requirements.txt # Dependencies
│── README.md

---

## 🔍 Key Features

### 📥 Log Ingestion
- Collects raw log data from system sources
- Handles structured and unstructured logs

### 🔎 Log Parsing & Processing
- Cleans and structures log data
- Extracts key fields (timestamps, IPs, events)

### 🚨 Threat Detection
- Detects:
  - Multiple failed login attempts (brute force)
  - Suspicious IP activity
  - Anomalous patterns

### 📊 Visualization
- Displays trends in:
  - Login activity
  - Alerts over time
  - Event frequency

---

## 🧪 Example Detection Use Case

### Brute Force Attack Detection
- Identifies repeated failed login attempts from a single IP
- Applies threshold-based detection logic
- Flags high-risk activity for investigation

**Outcome:**
- Suspicious IP identified
- Potential attack detected
- Ready for SOC escalation

---

## 🚀 Getting Started

### 1. Clone Repository
git clone https://github.com/fezphantom/security_siem_project.git

cd security_siem_project


### 2. Install Dependencies

pipenv install -r requirements.txt


### 3. Run Project

pipenv run streamlit run app.py


---

## 📊 Workflow


Load logs

Parse and clean data

Apply detection rules

Generate alerts

Visualize results


---

## 📈 Results

- Successfully detected **anomalous login patterns**
- Built an **end-to-end SIEM pipeline**
- Demonstrated ability to **analyze security logs**
- Simulated real-world **SOC monitoring workflows**

---

## ⚠️ Challenges

- Handling unstructured log formats  
- Reducing false positives in detection  
- Designing effective alert thresholds  

---

## 🔮 Future Improvements

- Real-time log streaming (Kafka / Logstash)  
- Machine learning-based anomaly detection  
- Cloud log integration (AWS / Azure)  
- Automated response (SOAR)  

---

## 💼 Why This Project Matters

This project demonstrates practical experience in:

- Security monitoring  
- Threat detection  
- Log analysis  
- SIEM systems  

It reflects the core responsibilities of a **SOC Analyst / Security Analyst** role.

---

## 👤 Author

**Peter Utomakili**  
Data Scientist | Aspiring Security Analyst  
GitHub: https://github.com/fezphantom

---

## 📄 License

MIT License

## Run Instructions
pip install -r requirements.txt
streamlit run app.py
