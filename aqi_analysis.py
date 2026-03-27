import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor , GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error , r2_score
import warnings
import pickle
warnings.filterwarnings('ignore')

# Load the dataset
df = pd.read_csv('city_day.csv')

# Basic Exploration
print("Shape:" , df.shape)
print("\nColumns:" , df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())
print("\nMissing values:")
print(df.isnull().sum())

# Data cleaning
# drop rows where AQI is missing 
df = df.dropna(subset=['AQI'])

# Save the best model
# fill the missing values with median
pollutants = ['PM2.5' , 'PM10' , 'NO' , 'NO2' , 'NOx' , 'NH3' , 'CO' , 'SO2' , 'O3' ,'Benzene' , 'Toluene' , 'Xylene']
for col in pollutants:
    df[col] = df[col].fillna(df[col].median())

print("\nAfter cleaning:")
print("Shape:" , df.shape)
print("Missing values:" , df.isnull().sum().sum())

#Visualization
plt.figure(figsize=(12,6))
city_aqi = df.groupby('City')['AQI'].mean().sort_values(ascending=False).head(10)
colors = plt.cm.RdYlGn(range(0,256,25))
bars = plt.bar(city_aqi.index,city_aqi.values,color = colors)
plt.title('Top 10 Most Polluted Cities in India (Average AQI)' , fontsize = 14,fontweight ='bold')
plt.xlabel('City')
plt.ylabel('Average AQI')
plt.xticks(rotation=45,ha='right')
plt.tight_layout()
plt.savefig('top_polluted_cities.png')
plt.close()
print("Chart saved: top_polluted_citiies.png")

#Visualization - AQI distribution
plt.figure(figsize=(10,5))
plt.hist(df['AQI'],bins=50,color='#e94560',edgecolor ='white',alpha =0.8)
plt.title('Distribution of AQI Values Across India' , fontsize=14,fontweight='bold')
plt.xlabel('AQI Value')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('aqi_distribution.png')
plt.close()
print("Chart saved: aqi_distribution.png")


# Model Training
# Select features and target
features = ['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene', 'Xylene']
X = df[features]
y = df['AQI']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train 3 models
models = {
    'Decision Tree': DecisionTreeRegressor(random_state=42),
    'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
    'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, random_state=42)
}

results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    mae = round(mean_absolute_error(y_test, preds), 2)
    r2 = round(r2_score(y_test, preds), 4)
    results[name] = {'MAE': mae, 'R2': r2}
    print(f"{name}: MAE={mae}, R2={r2}")

with open('rf_model.pkl', 'wb') as f:
    pickle.dump(models['Random Forest'], f)    
print("Model saved!")    

