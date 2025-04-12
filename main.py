import json

logs_path = "./logs/logs.json"

def read_logs(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            logs = json.load(file)
            return logs
    except FileNotFoundError:
        print(f"❌ Fayl topilmadi: {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ JSON xatosi: {e}")
        return None

logs = read_logs(logs_path)

if logs:
    print("🔍 Loglar:")
    for log in logs:
        print("\n", ("*" * 70), "\n")
        print(log)
else:
    print("❌ Loglar topilmadi yoki bo'sh.")