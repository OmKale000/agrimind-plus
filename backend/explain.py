# Simple explainability function for predictions

def explain_prediction(data, csi):
    reasons = []
    if data.ph < 5.5:
        reasons.append("Soil pH is too acidic")
    elif data.ph > 7.5:
        reasons.append("Soil pH is too alkaline")
    if data.moisture < 30:
        reasons.append("Low soil moisture")
    if data.temperature > 35:
        reasons.append("High temperature stress")
    if data.weather_forecast and "rain" in data.weather_forecast.lower():
        reasons.append("Forecasted rain helps reduce stress risk")
    if not reasons:
        reasons.append("All parameters within normal range")
    explanation = "Because " + ", ".join(reasons) + ", the Crop Stress Index is " + str(csi)
    return explanation
