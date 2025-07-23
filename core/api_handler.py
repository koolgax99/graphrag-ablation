import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

def call_chatbot_api(question, config, session_id=None):
    url = os.getenv("API_URL")

    payload = {
        'question': question,
        'session_id': session_id,
        'model': config['model'],
        'mode': config['mode'],
        'document_names': '[]',
        'uri': os.getenv("NEO4J_URI"),
        'database': os.getenv("NEO4J_DATABASE"),
        'userName': os.getenv("NEO4J_USERNAME"),
        'password': os.getenv("NEO4J_PASSWORD"),
        'temperature': str(config['temperature']),
        'top_k': config['top_k']
    }

    headers = {}
    files = []

    try:
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        response.raise_for_status()
        json_data = response.json()

        return json_data.get("data", {}).get("message", "No message found")

    except requests.exceptions.RequestException as e:
        return f"Request error: {str(e)}"
    except Exception as e:
        return f"Error parsing response: {str(e)}"
