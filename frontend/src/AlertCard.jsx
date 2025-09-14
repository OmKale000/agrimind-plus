function AlertCard({ alert }) {
  return (
    <div className="alert-card">
      <h3>Prediction Result</h3>
      <p><strong>Stress Risk:</strong> {alert.stress_risk}</p>
      <p><strong>Crop Stress Index:</strong> {alert.crop_stress_index}</p>
      <p><strong>Explanation:</strong> {alert.explanation}</p>
    </div>
  );
}
export default AlertCard;
