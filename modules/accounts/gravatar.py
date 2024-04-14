from lib.Requests import Request
from lib.colors import *
import hashlib

async def gravatar(target: str):
    
    encoded_email = target.lower().encode('utf-8')
    hashed_email = hashlib.sha256(encoded_email).hexdigest()

    r = await Request(f"https://en.gravatar.com/{hashed_email}.json").get()

    try:
        if "User not found" in r.text:
            print(f"{RED}>{WHITE} Gravatar")

        else:
            print(f"{GREEN}>{WHITE} Gravatar ~ Name : {r.json()['entry'][0]['displayName']}")
    
    except:
        pass