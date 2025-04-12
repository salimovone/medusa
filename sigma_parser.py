import yaml
import json
from helper import log

rule_path = "./rules/rule.yml"



def parse_sigma_rule(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            sigma_rule = yaml.safe_load(file)
            return sigma_rule
    except FileNotFoundError:
        print(f"❌ Fayl topilmadi: {file_path}")
        return None
    except yaml.YAMLError as e:
        print(f"❌ YAML xatosi: {e}")
        return None



def get_sections(rule_obj):
    res = []
    dumpDict = {}
    if rule_obj and "detection" in rule_obj:
        detection = rule_obj["detection"]
        for key, value in detection.items():
            if(key != "condition"):
                dumpDict[key] = value
            res.append(dumpDict)
        return dumpDict
    else:
        return None
    

"""malumotni tekshirish"""


def check_selections (selsections: dict, log: dict):
    if selsections:
        for key, value in log.items():
            print(f"value: {value}")



ruleInDict = parse_sigma_rule(rule_path)
sections = get_sections(ruleInDict)
log_dict = json.loads(log)

print(log_dict)

# check_selections(sections, log_dict)
