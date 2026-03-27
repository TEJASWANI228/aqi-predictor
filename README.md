# AQI Predictor

A Flask web application that predicts the Air Quality Index (AQI) using a Random Forest model trained on 12 pollutant features.

## Features

- Predicts AQI from 12 pollutant inputs: PM2.5, PM10, NO, NO2, NOx, NH3, CO, SO2, O3, Benzene, Toluene, Xylene
- Visual result with colour-coded AQI categories and a gradient bar
- Responsive two-column layout

## Local Setup

```bash
# 1. Clone the repository
git clone https://github.com/TEJASWANI228/aqi-predictor.git
cd aqi-predictor

# 2. Install dependencies
pip install -r requirements.txt

# 3. (Optional) Train the model
#    Place city_day.csv in the project root, then run:
python aqi_analysis.py

# 4. Start the development server
python app.py
```

Open `http://localhost:5000` in your browser.

## Deployment

### Render (recommended)

1. Push this repository to GitHub.
2. Go to [https://render.com](https://render.com) and create a **New Web Service**.
3. Connect your GitHub repository — Render will detect `render.yaml` automatically.
4. Click **Deploy**. Render installs dependencies with `pip install -r requirements.txt` and starts the app with `gunicorn app:app`.

> **Note:** The `/predict` API endpoint requires `rf_model.pkl`. Train the model locally (see step 3 above), commit `rf_model.pkl` to the repository, and redeploy. The home page works without the model file.

### Heroku

```bash
# Install the Heroku CLI, then:
heroku create your-app-name
git push heroku main
```

### Railway / Fly.io / any WSGI host

The `Procfile` (`web: gunicorn app:app`) is recognised by most Python hosting platforms. No extra configuration is needed beyond setting the environment variable `PORT` if required by the platform.

## Project Structure

```
aqi-predictor/
├── app.py              # Flask application
├── aqi_analysis.py     # Data exploration, visualisation & model training
├── requirements.txt    # Python dependencies
├── Procfile            # Gunicorn start command for deployment
├── render.yaml         # Render deployment configuration
└── templates/
    └── index.html      # Frontend UI
```
