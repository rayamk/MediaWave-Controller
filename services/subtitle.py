import os
import requests
from services.logger import get_logger

logger = get_logger("SubtitleTranslator")

def translate_subtitle(text, target_lang="Burmese"):
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        logger.error("API Key missing!")
        return "Error: API Key missing"
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    payload = {
        "contents": [{"parts": [{"text": f"Translate to {target_lang}. Only return the translation:\n{text}"}]}]
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        result = response.json()
        return result['candidates'][0]['content']['parts'][0]['text'].strip()
    except Exception as e:
        logger.error(f"API Error: {e}")
        return f"Error: {str(e)}"

