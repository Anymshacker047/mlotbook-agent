from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_reply(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a smart AI agent on Moltbook. Reply like a hacker + intelligent bot."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content