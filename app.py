from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = None
try:
    with open('rf_model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully!")
except FileNotFoundError:
    print("Warning: rf_model.pkl not found. /predict endpoint will not work.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model unavailable. Please contact the administrator.'}), 503
    try:
        data = request.get_json()
        features = [
            data['PM2.5'], data['PM10'], data['NO'],
            data['NO2'], data['NOx'], data['NH3'],
            data['CO'], data['SO2'], data['O3'],
            data['Benzene'], data['Toluene'], data['Xylene']
        ]
        prediction = model.predict([features])[0]
        aqi = round(float(prediction), 1)
        return jsonify({'aqi': aqi})
    except Exception as e:
        return jsonify({'error': str(e)}), 400  # ← what status code for a bad request?

if __name__ == '__main__':
    app.run(debug=False)