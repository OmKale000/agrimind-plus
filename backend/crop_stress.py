from typing import Tuple

# Dummy multi-modal fusion model for demo - replace with real model/inference
def predict_stress(data) -> Tuple[str, float]:
    """
    Input: SensorData object with soil and weather info
    Output: Tuple (str: risk message, float: crop stress index)
    """
    # Very basic simulation:
    # Crop Stress Index (CSI) between 0 and 1 (0 no risk, 1 max risk)
    csi = 0.0

    # Simple heuristic for demo based on inputs
    if data.ph < 5.5 or data.ph > 7.5:
        csi += 0.3
    if data.moisture < 30:
        csi += 0.4
    if data.temperature > 35:
        csi += 0.2

    # Weather impact
    if data.weather_forecast and "rain" in data.weather_forecast.lower():
        csi -= 0.3

    csi = max(0, min(1, csi))

    if csi > 0.7:
        risk = f"⚠️ High drought/pest/nutrient stress risk: {int(csi*100)}%"
    elif csi > 0.4:
        risk = f"⚠️ Moderate crop stress risk: {int(csi*100)}%"
    else:
        risk = "✅ Low crop stress risk"

    return risk, round(csi, 2)
