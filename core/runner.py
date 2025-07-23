import csv
from .api_handler import call_chatbot_api
from .utils import get_session_id
import random

def run_experiments(questions, configs, output_path, session):
    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["question_id", "question", "temperature", "model", "mode", "response"])
        
        for config in configs[:2]:
            for q in questions:

                session_id = get_session_id(q, config, session)

                print(f"[INFO] Running question ID: {q['id']} | Model: {config['model']} | Temp: {config['temperature']} | Mode: {config['mode']} | Session ID: {session_id}")

                response = call_chatbot_api(q["question"], config, session_id)
                
                writer.writerow([
                    q["id"],
                    q["question"],
                    config["temperature"],
                    config["model"],
                    config["mode"],
                    response
                ])
