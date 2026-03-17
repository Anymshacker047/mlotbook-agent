import time
import requests
from agent import generate_reply
from config import MOLTBOOK_API_URL, AGENT_NAME

def fetch_posts():
    try:
        res = requests.get(f"{MOLTBOOK_API_URL}/posts")
        return res.json()
    except:
        return []

def reply_to_post(post_id, text):
    try:
        requests.post(f"{MOLTBOOK_API_URL}/reply", json={
            "post_id": post_id,
            "text": text,
            "agent": AGENT_NAME
        })
    except:
        pass

def run_agent():
    print(f"[+] {AGENT_NAME} started...")
    
    while True:
        posts = fetch_posts()
        
        for post in posts[:5]:
            prompt = post.get("content", "")
            reply = generate_reply(prompt)
            
            print(f"[+] Replying to: {prompt}")
            reply_to_post(post["id"], reply)
        
        time.sleep(1800)  # 30 min

if __name__ == "__main__":
    run_agent()