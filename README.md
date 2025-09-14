# 🌱 AgriMind+ Crop Stress Early-Warning System
## 📖 Project Overview
AgriMind+ is an **AI-powered, multi-modal crop stress early-warning system** integrated with a conversational farming assistant (**FarmGPT**). It combines **soil sensor data, weather forecasts, and crop images** using machine learning to predict crop stress risks **3–7 days in advance**. The system provides **explainable alerts** and **personalized, natural language advice** to farmers via a **user-friendly web interface**.
---
## ✨ Features
- 🌾 **Multi-modal crop stress prediction** (drought, pest, nutrient stress) using sensor, weather, and image data  
- 🧠 **Explainable AI outputs** clarifying reasons behind stress alerts  
- 💬 **Conversational AI chatbot** for farmer queries with multilingual support  
- ⚡ **React-based frontend** with real-time alerts and interactive Q&A  
- 🏗️ **Modular, scalable, and extensible full-stack architecture**  
---
## 📂 Folder Structure
```
agrimind-plus/
├── backend/
│   ├── main.py           # FastAPI backend entrypoint and API logic
│   ├── crop_stress.py    # Crop stress prediction logic
│   ├── chatbot.py        # Conversational AI chatbot logic
│   ├── explain.py        # Explainability module for AI outputs
│   ├── requirements.txt  # Backend dependencies
├── frontend/
│   ├── public/
│   │   └── index.html    # Root HTML file
│   ├── src/
│   │   ├── App.js         # Main React app
│   │   ├── StressForm.jsx # Crop stress input form component
│   │   ├── Chatbot.jsx    # Chatbot UI component
│   │   ├── AlertCard.jsx  # Display prediction results and explanation
│   │   ├── index.js       # React entrypoint
│   │   ├── App.css        # Styling
│   ├── package.json       # Frontend dependencies
├── README.md
```
---
## Setup Instructions
### Backend
1. Navigate to the `backend` folder:
```
cd backend
```
3. Create and activate a Python virtual environment (optional):
- Windows PowerShell:
```
python -m venv venv
.\venv\Scripts\Activate.ps1
```
- Linux/macOS:
```
python3 -m venv venv
source venv/bin/activate
```
3. Install dependencies:
```
pip install -r requirements.txt
```
4. Run backend server:
```
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
5. Access API docs at [http://localhost:8000/docs](http://localhost:8000/docs)
### Frontend
1. Navigate to the `frontend` folder:
```
cd ../frontend
```
3. Install dependencies:
```
npm install
```
5. Run frontend server:
```
npm start
```
7. Open your browser at [http://localhost:3000](http://localhost:3000)
---
## Usage
- Use the Crop Stress Prediction form to input soil pH, moisture, temperature, and weather forecast. Submit to receive risk alert and explanation.  
- Use the FarmGPT conversational assistant to ask natural language questions about your crop or farming practices and get AI-generated advice.  
---
## Technologies Used
### Backend & AI
- FastAPI  
- TensorFlow / PyTorch (for ML models)  
- OpenAI GPT / HuggingFace Transformers (chatbot)  
- Uvicorn ASGI server
### Frontend & Development
- React.js  
- JavaScript (ES6+)  
- npm, pip  
- Git  
---
## Improvisations Done
- Modular full-stack design enabling rapid development  
- Dummy multi-modal AI model with explainable predictions  
- FarmGPT chatbot with multilingual, natural language support  
- Added CORS for seamless frontend-backend integration  
- Enhanced UI with modern styling and responsive layout  
- Robust API endpoints with error handling  
---
## Author & Contact :
---
Om Kale

Email: ok176471@gmail.com

LinkedIn: [linkedin.com/in/om-kale-1663a0276](https://linkedin.com/in/om-kale-1663a0276)

GitHub: [github.com/OmKale](https://github.com/OmKale)

---
Thank you for exploring AgriMind+ — empowering farmers with AI-driven, explainable, and personalized crop stress advisories!
