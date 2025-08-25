import os

from core.utils import load_questions, load_configs
from core.runner import run_experiments

base_dir = os.path.dirname(os.path.abspath(__file__))
questions = load_questions(os.path.join(base_dir, "data/questions.csv"))
configs = load_configs(os.path.join(base_dir, "config/study_config.yaml"))

run_experiments(questions, configs, os.path.join(base_dir, "outputs/metric_results_v2.csv"), session="unique")
