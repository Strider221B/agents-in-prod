import os
from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from openai import OpenAI

load_dotenv(override=True)

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def instant() -> str:

    client = OpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
                    api_key=os.getenv('GOOGLE_API_KEY'))

    message = ("You are on a website that has just been deployed to production for the first time! "
               "Please reply with an enthusiastic announcement to welcome visitors to the site, "
               "explaining that it is live on production for the first time!")

    messages = [{"role": "user", "content": message}]
    response = client.chat.completions.create(model='gemini-2.5-flash-lite-preview-09-2025', messages=messages)
    reply = response.choices[0].message.content.replace("\n", "<br/>")
    html = f"<html><head><title>Live in an Instant!</title></head><body><p>{reply}</p></body></html>"
    return html

