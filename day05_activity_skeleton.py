"""
Day 5 Activity: JSON + File Handling mini workflow.
Tasks:
1) Load training config from JSON
2) Simulate training results (dict)
3) Save results to JSON safely
"""

import json
from pathlib import Path

# TODO: Load config.json from disk
# TODO: Print config values
# TODO: Create results dict and write to results.json

# Hint: use Path and with open(...)

import json
from pathlib import Path

# TODO: Load config.json from disk
config_path = Path("config.json")
with open(config_path, "r") as f:
    config = json.load(f)

# TODO: Print config values
print(config)

# TODO: Create results dict and write to results.json
results = {
    "model": config["model"],
    "epochs": config["epochs"],
    "accuracy": 0.92,
    "loss": 0.15
}

results_path = Path("results.json")
with open(results_path, "w") as f:
    json.dump(results, f, indent=2)