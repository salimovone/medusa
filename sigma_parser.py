import yaml
from helper import logs

rule_path = "./rules/rule.yml"
log = logs[5]


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
    logDataDump = list(log["Message"])
    logData = dict()
    for i in logDataDump[0].split("\r\n"):
        iList = i.split(": ")
        if len(iList) > 1:
            logData[iList[0]] = iList[1]
    
    # for key, value in logData.items():
    #     print(f"{key}: {value} \n")
    
    for key, value in selsections.items():
        # print(list(dict(value).items()))
        check_log(logData, list(dict(value).items()))
        
        
def check_log(logData : dict, rule):
    rule = list(rule[0])
    modifier = rule[0].split("|")
    field = rule[1]
    if not logData.get(modifier[0], False):
        return False
    logField = logData[modifier[0]]
    
    if "cased" in modifier:
        for i in field:
            print(i == logField)
    if "contains" in modifier:
        for i in field:
            print(i.lower() in logField.lower())
    if "startswith" in modifier:
        for i in field:
            print(logField.startswith(i))
    if "endswith" in modifier:
        for i in field:
            print(logField.endswith(i))
    if "matches" in modifier:
        for i in field:
            print(logField == i)
    # if "equals" in modifier:
        
        


ruleInDict = parse_sigma_rule(rule_path)
sections = get_sections(ruleInDict)


check_selections(sections, log)
