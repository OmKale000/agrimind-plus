import React, { useState } from "react";

function Chatbot() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!question.trim()) return;
    setLoading(true);

    try {
      const res = await fetch("http://localhost:8000/api/chatbot", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: question.trim() }),
      });
      const data = await res.json();
      if (res.ok) {
        setResponse(data.response);
      } else {
        setResponse("Error: " + data.detail);
      }
    } catch (err) {
      setResponse("Network error");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>FarmGPT Conversational Assistant</h2>
      <textarea
        rows="3"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask about your crop or farming advice..."
        style={{ width: "100%" }}
      />
      <button onClick={handleAsk} disabled={loading || !question.trim()}>
        {loading ? "Thinking..." : "Ask"}
      </button>
      {response && (
        <div className="chat-response">
          <strong>Response:</strong> <p>{response}</p>
        </div>
      )}
    </div>
  );
}

export default Chatbot;
