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
        'write_access': 'true',
        'evaluation': 'true'
    }

    headers = {}
    files = []

    try:
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        response.raise_for_status()
        json_data = response.json()

        message = json_data.get("data", {}).get("message", "No message found")
        metrics = json_data.get("data", {}).get("info", {}).get("metrics", {}).get("scores", {})
        response_time = json_data.get("data", {}).get("info", {}).get("response_time", {})
        message_time = json_data.get("data", {}).get("info", {}).get("message_time", {})

        return message, metrics[0], response_time, message_time 

    except requests.exceptions.RequestException as e:
        return f"Request error: {str(e)}", {}, {}, {}
    except Exception as e:
        return f"Error parsing response: {str(e)}", {} , {}, {}

def call_async_chatbot_api(question, config, session_id=None):
    url = os.getenv("ASYNC_API_URL")

    payload = {
        'question': question,
        'session_id': session_id,
        'model': config['model'],
        'mode': 'graph_of_thought',
        'document_names': '[]',
        'uri': os.getenv("NEO4J_URI"),
        'database': os.getenv("NEO4J_DATABASE"),
        'userName': os.getenv("NEO4J_USERNAME"),
        'password': os.getenv("NEO4J_PASSWORD"),
        'temperature': str(config['temperature']),
        'write_access': 'true',
        'evaluation': 'true'
    }

    headers = {}
    files = []

    try:
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        response.raise_for_status()
        json_data = response.json()

        message = json_data.get("data", {}).get("message", "No message found")
        metrics = json_data.get("data", {}).get("info", {}).get("metrics", {}).get("scores", {})
        response_time = json_data.get("data", {}).get("info", {}).get("response_time", {})
        message_time = json_data.get("data", {}).get("info", {}).get("message_time", {})

        return message, metrics[0], response_time, message_time 

    except requests.exceptions.RequestException as e:
        return f"Request error: {str(e)}", {}
    except Exception as e:
        return f"Error parsing response: {str(e)}", {}