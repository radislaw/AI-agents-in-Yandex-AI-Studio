import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

folder_id = os.environ["folder_id"]
api_key = os.environ["api_key"]

client = OpenAI(
   base_url = "https://ai.api.cloud.yandex.net/v1",
   api_key = api_key,
   project = folder_id
)

model = f"gpt://{folder_id}/yandexgpt/rc"

res = client.responses.create(
    model = model,
    input = "Как тренироваться, чтобы сбросить вес?"
)
print(res.output_text)
