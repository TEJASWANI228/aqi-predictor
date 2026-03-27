# 🌍 AQI Predictor — Air Quality Intelligence

> Predict air quality in real-time using machine learning trained on Indian city data.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey)
![ML](https://img.shields.io/badge/Model-Random%20Forest-green)
![R2](https://img.shields.io/badge/R²%20Score-0.908-brightgreen)

---

## 🎯 What Is This?

AQI Predictor is a full-stack machine learning web application that predicts
the **Air Quality Index (AQI)** of a location based on 12 pollutant readings.

Enter real pollutant values → Get instant AQI prediction → See color-coded
health advice.

---

## ✨ Features

- 🔬 **ML-Powered** — Random Forest model with R² = 0.908
- 🎨 **Color-coded Results** — Green to Hazardous based on AQI level
- 💻 **Clean Dashboard UI** — Sky-themed responsive interface
- ⚡ **Real-time Prediction** — Instant results via Flask REST API
- 📊 **Trained on Real Data** — city_day.csv with Indian city pollution data

---

## 🧠 Model Details

| Property | Value |
|----------|-------|
| Algorithm | Random Forest Regressor |
| R² Score | **0.908** |
| Training Data | city_day.csv |
| Input Features | 12 pollutants |
| Output | AQI Value (0–500) |

### 📥 Input Features
| Feature | Unit | Description |
|---------|------|-------------|
| PM2.5 | µg/m³ | Fine particulate matter |
| PM10 | µg/m³ | Coarse particulate matter |
| NO | µg/m³ | Nitric oxide |
| NO2 | µg/m³ | Nitrogen dioxide |
| NOx | ppb | Nitrogen oxides |
| NH3 | µg/m³ | Ammonia |
| CO | mg/m³ | Carbon monoxide |
| SO2 | µg/m³ | Sulfur dioxide |
| O3 | µg/m³ | Ozone |
| Benzene | µg/m³ | Benzene |
| Toluene | µg/m³ | Toluene |
| Xylene | µg/m³ | Xylene |

---

## 🎨 AQI Categories

| AQI Range | Category | Health Impact |
|-----------|----------|---------------|
| 0–50 | 🟢 Good | Minimal impact |
| 51–100 | 🟡 Moderate | Acceptable |
| 101–150 | 🟠 Unhealthy for Sensitive Groups | Sensitive people at risk |
| 151–200 | 🔴 Unhealthy | Everyone affected |
| 201–300 | 🟣 Very Unhealthy | Health alert |
| 300+ | ⚫ Hazardous | Emergency conditions |

---

## 🛠️ Tech Stack

**Backend**
- Python 3
- Flask
- Scikit-learn
- NumPy & Pandas
- Pickle

**Frontend**
- HTML5 & CSS3
- Vanilla JavaScript
- Fetch API

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed
- pip package manager

### Installation

1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/aqi-predictor.git
cd aqi-predictor
```

2. Install dependencies
```bash
pip install flask scikit-learn numpy pandas
```

3. Run the application
```bash
python app.py
```

4. Open your browser
```
http://127.0.0.1:5000
```

---

## 📁 Project Structure
```
aqi-predictor/
├── app.py                 # Flask backend & REST API
├── aqi_analysis.py        # Data cleaning, EDA & model training
├── rf_model.pkl           # Trained Random Forest model
├── README.md              # Project documentation
└── templates/
    └── index.html         # Frontend dashboard
```

---

## 📊 Model Training Process

1. **Data Loading** — Loaded city_day.csv with Indian city pollution data
2. **Data Cleaning** — Dropped rows with missing AQI, filled pollutant nulls with median
3. **Visualization** — Plotted top polluted cities and AQI distribution
4. **Model Training** — Trained 3 models and compared performance
5. **Model Selection** — Random Forest selected with best R² = 0.908
6. **Deployment** — Exported model with pickle, served via Flask

---

## 👤 Author

**Your Name**
- GitHub: [TEJASWANI228}(https://github.com/TEJASWANI228)

---
⭐ If you found this useful, please star the repository!
