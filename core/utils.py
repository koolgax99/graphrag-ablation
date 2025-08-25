import csv
import yaml
import itertools

def load_questions(csv_path):
    with open(csv_path, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)

def load_configs(yaml_path):
    with open(yaml_path, "r") as f:
        raw = yaml.safe_load(f)["parameters"]
    
    # Turn list of dicts into one merged dict
    param_dict = {}
    for d in raw:
        param_dict.update(d)

    # Cartesian product of all values
    keys = param_dict.keys()
    values = param_dict.values()
    combinations = list(itertools.product(*values))

    # Return list of dict configs
    configs = [dict(zip(keys, combo)) for combo in combinations]
    return configs

def get_session_id(question, config, session_type):
    import random
    temperature_str = str(config['temperature']).replace('.', '')
    session_id = (
        f"{question['session_id']}-"
        f"{config['model']}-"
        f"{temperature_str}-"
        f"{config['mode']}-"
    )

    if session_type == "unique":
        return f"{session_id}-{random.randint(1000, 9999)}"
    else:
        return session_id

