import os
import json
from sigma_matcher import load_sigma_rule, match_log_to_rule

RULES_DIR = 'rules'
LOG_FILE = 'logs/logs.json'  # endi .json

def load_all_rules(dir_path):
    rules = []
    for fname in os.listdir(dir_path):
        if fname.endswith('.yml') or fname.endswith('.yaml'):
            full_path = os.path.join(dir_path, fname)
            rule = load_sigma_rule(full_path)
            rules.append((fname, rule))
    return rules

def scan_logs(log_file_path, rules):
    with open(log_file_path, 'r', encoding='utf-8') as f:
        logs = json.load(f)

    for i, log in enumerate(logs, 1):
        for rule_name, rule in rules:
            if match_log_to_rule(log, rule):
                print(f"🚨 [{i}-log] Xavfli log (Qoida: {rule_name}):\n{json.dumps(log, indent=2)}\n")

if __name__ == '__main__':
    rules = load_all_rules(RULES_DIR)
    scan_logs(LOG_FILE, rules)
