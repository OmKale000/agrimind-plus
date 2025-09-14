# Simple chatbot logic (stub for LLM integration)
# You can integrate with OpenAI GPT or local LLM API here

def chatbot_response(question: str, language: str = "en") -> str:
    """
    Returns a canned or dummy response based on the question for demo.
    Replace this with actual LLM integration using OpenAI or HuggingFace.
    """
    q = question.lower()
    if "why" in q and "risk" in q:
        return "The risk is flagged based on low moisture, abnormal soil pH, and weather conditions causing drought stress."
    elif "fertilizer" in q:
        return "Applying nitrogen-rich fertilizer is recommended for nutrient-deficient soils."
    elif "irrigate" in q:
        return "Irrigation is advised tomorrow if soil moisture remains below 40%."
    else:
        return "Sorry, I am still learning. Please ask about crop stress or fertilizer advice."
