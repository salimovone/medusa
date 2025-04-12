import yaml
import re

def parse_message_field(message_raw):
    """
    'Message' maydoni dict bo‘lsa `Description`ni, str bo‘lsa o‘zini ishlatadi.
    """
    if isinstance(message_raw, dict):
        # dict ichida 'Description' bor yoki yo‘qligini tekshir
        message_str = message_raw.get("Description", "")
    elif isinstance(message_raw, str):
        message_str = message_raw
    else:
        message_str = ""

    result = {}
    lines = message_str.split('\r\n')
    for line in lines:
        if ": " in line:
            key, val = line.split(": ", 1)
            result[key.strip()] = val.strip()
    return result


def load_sigma_rule(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def match_log_to_selection(log, selection):
    for key, val in selection.items():
        # Misol uchun 'Image|contains' => 'Image'
        real_key = key.split('|')[0]

        if real_key not in log:
            return False

        # 🔽 val turini tekshiramiz
        if isinstance(val, list):
            # Har bir ro‘yxat elementini tekshiramiz
            if not any(str(v).lower() in str(log[real_key]).lower() for v in val):
                return False
        else:
            # Oddiy qiymat bo‘lsa
            if str(val).lower() not in str(log[real_key]).lower():
                return False
    return True


def match_log_to_rule(raw_log, rule: dict) -> bool:
    # 'Message' matnini dict ga aylantiramiz
    message_dict = parse_message_field(raw_log.get('Message', ''))

    
    # Boshqa metadata ham qo‘shamiz
    combined_log = {**raw_log, **message_dict}

    detection = rule.get('detection', {})
    condition = detection.get('condition')

    if isinstance(condition, str) and condition == 'selection':
        selection = detection.get('selection', {})
        return match_log_to_selection(combined_log, selection)

    matches = {}
    for sel_key, sel_val in detection.items():
        if sel_key == 'condition':
            continue
        matches[sel_key] = match_log_to_selection(combined_log, sel_val)

    if condition:
        try:
            return eval(condition, {}, matches)
        except Exception as e:
            print(f"❌ Eval xatosi: {e}")
            return False
    
    return False
