from google import genai

from config import API_KEY
from memory import add_message, load_history

client = genai.Client(api_key=API_KEY)

MODEL = "gemini-flash-latest"


def ask_gemini(user_message):

    history = load_history()

    conversation = ""

    for msg in history:
        conversation += f"{msg['role']}: {msg['content']}\n"

    prompt = f"""
You are a professional AI assistant.

Conversation:

{conversation}

User:
{user_message}
"""

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )

        answer = response.text

    except Exception as e:
        answer = str(e)

    add_message("User", user_message)
    add_message("Assistant", answer)

    return answer