import os
import time
import random
import openai
import requests

delay = random.randint(0, 60)
print(f"Delaying for {delay} seconds before sending mantra...")
time.sleep(delay)

openai_api_key = os.environ["OPENAI_API_KEY"]
telegram_bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
telegram_chat_id = os.environ["TELEGRAM_CHAT_ID"]

client = openai.OpenAI(api_key=openai_api_key)
model = random.choice(["gpt-3.5-turbo", "gpt-4-turbo"])
print(f"Using model: {model}")

response = client.chat.completions.create(
    model = model,
    messages=[{
        "role": "user",
        "content": (
            "Give me one deep, thought-provoking quote from 'The Monk Who Sold His Ferrari' or a similar spiritual/self-development book. "
            "It should feel calming, grounded, and wise. The quote should be between 10 to 25 words long. Avoid clichés or generic motivational phrases.")
    }])
print("OpenAI response:", response)

mantra = response.choices[0].message.content.strip()
print("Mantra extracted:", mantra)

message = f"🧘‍♀️ {mantra}"
print("Telegram message composed:", message)

tg_response = requests.post(
    f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage",
    data={"chat_id": telegram_chat_id, "text": message}
)
print("Telegram response code:", tg_response.status_code)
print("Telegram response body:", tg_response.text)
