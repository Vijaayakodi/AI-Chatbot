import json
from pathlib import Path

FILE = Path("data/chat_history.json")


def load_history():
    if not FILE.exists():
        return []

    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def save_history(history):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4)


def add_message(role, content):
    history = load_history()

    history.append({
        "role": role,
        "content": content
    })

    history = history[-20:]

    save_history(history)


def clear_history():
    save_history([])