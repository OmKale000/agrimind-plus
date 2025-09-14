import React, { useState } from "react";

function StressForm({ onResult }) {
  const [ph, setPh] = useState("");
  const [moisture, setMoisture] = useState("");
  const [temperature, setTemperature] = useState("");
  const [weather, setWeather] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const payload = {
      ph: parseFloat(ph),
      moisture: parseFloat(moisture),
      temperature: parseFloat(temperature),
      weather_forecast: weather,
    };

    try {
      const res = await fetch("http://localhost:8000/api/predict_stress", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      const data = await res.json();
      if (res.ok) {
        onResult(data);
      } else {
        alert("Error: " + data.detail);
      }
    } catch (err) {
      alert("Network error");
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: 20 }}>
      <h2>Crop Stress Prediction Input</h2>
      <label>
        Soil pH:
        <input type="number" step="0.1" value={ph} onChange={(e) => setPh(e.target.value)} required />
      </label>
      <br />
      <label>
        Soil Moisture (%):
        <input type="number" step="0.1" value={moisture} onChange={(e) => setMoisture(e.target.value)} required />
      </label>
      <br />
      <label>
        Temperature (°C):
        <input type="number" step="0.1" value={temperature} onChange={(e) => setTemperature(e.target.value)} required />
      </label>
      <br />
      <label>
        Weather Forecast (e.g., sunny, rainy):
        <input type="text" value={weather} onChange={(e) => setWeather(e.target.value)} />
      </label>
      <br />
      <button type="submit">Predict Stress</button>
    </form>
  );
}

export default StressForm;
