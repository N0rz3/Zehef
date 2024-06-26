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
            data = r.json()['entry'][0]

            print(f"{GREEN}>{WHITE} Gravatar")
            print(f"  ├──> Username : {data['displayName']}")

            try:
                avatar_url_seaked = data['thumbnailUrl']
                avatar_url = str(avatar_url_seaked).replace("\\", "")

                print(f"  ├──> Avatar : {avatar_url}")

            except:
                pass

            print(f"  └──> Account : {CYAN}https://gravatar.com/{data['displayName']}/{WHITE}")

    except:
        print(f"{RED}>{WHITE} Gravatar")