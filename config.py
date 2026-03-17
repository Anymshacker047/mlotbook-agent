import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MOLTBOOK_API_URL = os.getenv("MOLTBOOK_API_URL")
AGENT_NAME = os.getenv("AGENT_NAME")