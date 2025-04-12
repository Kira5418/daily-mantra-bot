import os
import time
import random
import openai
import requests
import datetime

# Random delay: up to 8 hours (0–28800 seconds)
delay = random.randint(0, 28800)
time.sleep(delay)

# OpenAI setup
openai.api_key = os.environ["OPEN_API_KEY"]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{
        "role": "user",
        "content": (
            "Give me one deep, thought-provoking quote from 'The Monk Who Sold His Ferrari' or a similar spiritual/self-development book. "
            "It should feel calming, grounded, and wise. The quote should be between 10 to 25 words long. Avoid clichés or generic motivational phrases."
        )
    }]
)

quote = response.choices[0].message["content"].strip()

# Telegram setup
telegram_bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
telegram_chat_id = os.environ["TELEGRAM_CHAT_ID"]

message = f"🧘‍♀\n\n{quote}"

requests.post(
    f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage",
    data={"chat_id": telegram_chat_id, "text": message}
)
