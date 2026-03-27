# 🌍 Air Quality Index (AQI) Predictor
### A Machine Learning Web Application for Real-time Pollutant Analysis

[![Live Demo](https://img.shields.io/badge/Demo-Live%20on%20Render-informational)](YOUR_RENDER_URL_HERE)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Framework](https://img.shields.io/badge/Framework-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)

## 📌 Project Overview
This project is a full-stack Machine Learning application that predicts the **Air Quality Index (AQI)** based on 12 different pollutant levels (PM2.5, PM10, CO, NO2, etc.). It uses a **Random Forest Regressor** trained on historical environmental data to provide high-accuracy predictions.

## 🚀 Features
* **ML Model:** Random Forest Regressor with an $R^2$ score of **0.908**.
* **Responsive UI:** Custom CSS-designed dashboard with dynamic cloud/sun animations.
* **Real-time Prediction:** Uses Fetch API to communicate between the browser and the Flask backend.
* **AQI Categorization:** Automatically classifies results into "Good," "Moderate," or "Hazardous" with health recommendations.

## 🛠️ Tech Stack
* **Frontend:** HTML5, CSS3, JavaScript (ES6+)
* **Backend:** Flask, Gunicorn
* **Machine Learning:** Scikit-learn, Pandas, NumPy, Pickle
* **Deployment:** Render (Cloud Platform)

## 📊 Data Features (Inputs)
The model accepts 12 major pollutants:
`PM2.5`, `PM10`, `NO`, `NO2`, `NOx`, `NH3`, `CO`, `SO2`, `O3`, `Benzene`, `Toluene`, `Xylene`.

## ⚙️ Local Setup
1. Clone the repo: `git clone https://github.com/YOUR_USERNAME/aqi-predictor.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `python app.py`
4. Access at: `http://127.0.0.1:5000`

---
*Developed as part of my Engineering Coursework at VIT Bhopal University.*
