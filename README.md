# Health Monitoring and Activity Recognition System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Dash](https://img.shields.io/badge/Dash-3.x-orange)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.2-green)

## Project Overview

This project simulates a **smart healthcare monitoring system** using Python. It monitors physiological data such as **heart rate, body temperature, and motion**, and recognizes activities like **resting, walking, and exercising**. The system also provides **health alerts** if abnormal readings are detected.

The project consists of:

- **Machine Learning model** (Random Forest) trained on simulated wearable sensor data.
- **Interactive dashboard** built with Dash to visualize live readings and activity predictions.
- **Health alert system** to warn when heart rate or temperature is abnormal.
- Fully **Python-based** implementation for demonstration and portfolio purposes.

---

## Features

- Simulates sensor readings for heart rate, temperature, and acceleration.
- Predicts activity in real-time: `resting`, `walking`, or `exercising`.
- Displays alerts when physiological readings are abnormal.
- Live updating dashboard with interactive components.
- Modular code structure for easy extension with real sensor data in the future.

---

## Project Structure
```text
health_monitoring_system/
├─ app/
│  └─ dashboard.py        # Dash dashboard
├─ models/
│  └─ activity_model.pkl  # Trained Random Forest model
├─ notebooks/
│  └─ model_training.ipynb # Notebook to generate model
├─ data/
│  └─ sensor_data.csv     # Simulated sensor data
├─ requirements.txt       # Python dependencies
└─ README.md              # Project documentation
```

## Installation

### Clone the repository:

- git clone https://github.com/MitaliHukkeri/health_monitoring_system.git
cd health_monitoring_system


### Create and activate a virtual environment:

- python -m venv venv
- venv\Scripts\activate      # Windows
- source venv/bin/activate   # macOS/Linux


### Install dependencies:

- pip install -r requirements.txt

## Usage

### Run the dashboard:

- python app\dashboard.py


### Open your browser at:

- http://127.0.0.1:8050/


How It Works:
- **Sensor Data Simulation:** Randomized heart rate, temperature, and motion acceleration values are generated.
- **Model Training:** Random Forest model classifies activities (resting, walking, exercising).
- **Dashboard Updates:** Dash callbacks fetch new simulated data every 3 seconds, predict activity, and show alerts.
