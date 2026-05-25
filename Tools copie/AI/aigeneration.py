from openrouter import OpenRouter
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("OPENROUTER_API_KEY manquante")

history = [
    {
        "role": "system",
        "content": (
            "Tu réponds toujours en français. "
            "Réponds de façon concise : 2 à 6 phrases maximum. "
            "Va droit au but."
            "Répond toujour de façon amicale et pas trop brusque"
            "Inclue des emojis dans tes message mais pas trop"
        )
    }
]

def show_contexte():
    return history

def send_message(message: str):
    history.append({
        "role": "user",
        "content": message
    })

    with OpenRouter(api_key=api_key.strip()) as client:
        response = client.chat.send(
            model="sao10k/l3-lunaris-8b",
            messages=history,
            max_completion_tokens=150
        )

    answer = response.choices[0].message.content
    history.append({
        "role": "assistant",
        "content": answer
    })

    return answer