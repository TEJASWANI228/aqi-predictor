# 🌫️ AQI Predictor — Air Quality Index Prediction Web App

A machine learning web application that predicts the **Air Quality Index (AQI)** based on pollutant concentrations using a trained **Random Forest model**.

## 🚀 Live Demo
🔗 [Click here to view the live app](https://aqi-predictor.onrender.com)

## 📌 Project Overview
Air pollution is one of the biggest environmental challenges. This project uses real-world air quality data to train a machine learning model that can predict AQI from pollutant readings.

## ✨ Features
- 🔬 Predicts AQI from 12 pollutant inputs
- 🎨 Beautiful dashboard UI with sky theme
- 📊 Visual AQI gauge with color-coded categories
- ⚡ Real-time prediction with animated results
- 📱 Responsive design

## 🤖 ML Model Performance
| Model | R² Score |
|-------|----------|
| Random Forest ⭐ | **0.908** |

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **ML:** Scikit-learn, Pandas, NumPy
- **Deployment:** Render

## ⚙️ How to Run Locally
1. Clone the repo: `git clone https://github.com/TEJASWANI228/aqi-predictor.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Train model: `python aqi_analysis.py`
4. Run app: `python app.py`
5. Open browser: `http://127.0.0.1:5000`

> ⚠️ Note: rf_model.pkl is not included (140MB). Run aqi_analysis.py first to generate it.

## 📊 AQI Categories
| AQI Range | Category |
|-----------|----------|
| 0 - 50 | 🟢 Good |
| 51 - 100 | 🟡 Moderate |
| 101 - 150 | 🟠 Unhealthy for Sensitive |
| 151 - 200 | 🔴 Unhealthy |
| 201 - 300 | 🟣 Very Unhealthy |
| 301 - 500 | 🔴 Hazardous |

## 👩‍💻 Developed By
**Tejaswani** — GitHub: [@TEJASWANI228](https://github.com/TEJASWANI228)
