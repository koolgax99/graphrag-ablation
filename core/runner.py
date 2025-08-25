import csv
from .api_handler import call_chatbot_api, call_async_chatbot_api
from .utils import get_session_id
import random
import re

def strip_think_block(text):
    return re.sub(r'<think>[\s\S]*?</think>', '', text, flags=re.DOTALL).strip()

def run_experiments(questions, configs, output_path, session):
    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["question_id", "question", "temperature", "model", "mode", "response", "answer_relevancy", "faithfulness", "llm_context_precision_without_reference", "nv_context_relevance", "nv_response_groundedness", "total_response_time", "total_retrieval_time"])
        
        for config in configs:
            for q in questions:

                session_id = get_session_id(q, config, session)

                print(f"[INFO] Running question ID: {q['id']} | Model: {config['model']} | Temp: {config['temperature']} | Mode: {config['mode']} | Session ID: {session_id}")

                response, metrics, response_time, message_time = call_chatbot_api(q["question"], config, session_id)

                response = strip_think_block(response)

                writer.writerow([
                    q["id"],
                    q["question"],
                    config["temperature"],
                    config["model"],
                    config["mode"],
                    response,
                    metrics.get("answer_relevancy", 0),
                    metrics.get("faithfulness", 0),
                    metrics.get("llm_context_precision_without_reference", 0),
                    metrics.get("nv_context_relevance", 0),
                    metrics.get("nv_response_groundedness", 0),
                    response_time,
                    message_time
                ])

                # if config["mode"] == "graph_of_thought":
                #     async_response, async_metrics, async_response_time, async_message_time = call_async_chatbot_api(q["question"], config, session_id)

                #     async_response = strip_think_block(async_response)

                #     writer.writerow([
                #         q["id"],
                #         q["question"],
                #         config["temperature"],
                #         config["model"],
                #         "optimized_graph_of_thought",
                #         async_response,
                #         async_metrics.get("answer_relevancy", 0),
                #         async_metrics.get("faithfulness", 0),
                #         async_metrics.get("llm_context_precision_without_reference", 0),
                #         async_metrics.get("nv_context_relevance", 0),
                #         async_metrics.get("nv_response_groundedness", 0),
                #         async_response_time,
                #         async_message_time
                #     ])
