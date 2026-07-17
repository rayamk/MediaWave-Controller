import os
import google.generativeai as genai
from services.logger import get_logger

USE_MOCK_MODE = False 

logger = get_logger("SubtitleTranslator")

def translate_subtitle(text, target_lang="Burmese"):
    if USE_MOCK_MODE:
        logger.info("Mock Mode: Returning dummy translation.")
        return f"[Translated in Mock Mode] {text}"

    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        logger.error("API Key missing in environment!")
        return "Error: Configuration Error"
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"Translate to {target_lang}. Only return the translation:\n{text}"
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        logger.error(f"API Error: {e}")
        return f"Error: {str(e)}"

