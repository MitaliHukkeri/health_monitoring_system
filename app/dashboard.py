# dashboard.py
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import random
import pandas as pd
import joblib
import os

# Load the trained model (path relative to this file)
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../models/activity_model.pkl')
model = joblib.load(model_path)

# Function to generate health alerts
def check_alert(heart_rate, temperature):
    alerts = []
    if heart_rate > 140:
        alerts.append("⚠️ High heart rate! Possible overexertion.")
    if temperature > 100.4:
        alerts.append("🌡️ High body temperature! Possible fever.")
    if not alerts:
        alerts.append("✅ All vitals normal.")
    return alerts

# Create Dash app
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Health Monitoring Dashboard"),
    html.Div(id='live-data'),
    dcc.Interval(id='interval-component', interval=3000, n_intervals=0)  # updates every 3 sec
])

@app.callback(
    Output('live-data', 'children'),
    Input('interval-component', 'n_intervals')
)
def update_data(n):
    # Simulate new sensor readings
    heart_rate = random.randint(60, 160)
    temperature = random.uniform(97.0, 101.5)
    acceleration = random.uniform(0.1, 5.0)

    # Predict activity using saved model
    sample = pd.DataFrame([[heart_rate, temperature, acceleration]],
                          columns=['heart_rate','temperature','acceleration'])
    pred_encoded = model.predict(sample)[0]
    pred_label = ['resting', 'walking', 'exercising'][pred_encoded]

    # Check for alerts
    alerts = check_alert(heart_rate, temperature)

    # Return dashboard content
    return html.Div([
        html.H3(f"Heart Rate: {heart_rate} bpm"),
        html.H3(f"Temperature: {temperature:.1f} °F"),
        html.H3(f"Predicted Activity: {pred_label}"),
        html.H4(" | ".join(alerts))
    ])

# Run the server
if __name__ == '__main__':
    app.run(debug=True)

