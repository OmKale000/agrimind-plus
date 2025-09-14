import React, { useState } from "react";
import StressForm from "./StressForm";
import Chatbot from "./Chatbot";
import AlertCard from "./AlertCard";
import "./App.css";

function App() {
  const [alert, setAlert] = useState(null);

  const handleStressResult = (result) => {
    setAlert(result);
  };

  return (
    <div className="container">
      <h1>AgriMind+ Crop Stress Early-Warning</h1>
      <StressForm onResult={handleStressResult} />
      {alert && <AlertCard alert={alert} />}
      <hr />
      <Chatbot />
    </div>
  );
}

export default App;
