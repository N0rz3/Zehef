from lib.Requests import Request
from lib.colors import *

async def picsart(target: str):

    params = {
        'email_encoded': 1,
        'emails': target
    }

    r = await Request("https://api.picsart.com/users/email/existence", params=params).get()

    print(r.json())

    if r.json()['status'] == 'success':
        
        if r.json()['response']:
            print(f"{GREEN}>{WHITE} Picsart")

        else:
            print(f"{RED}>{WHITE} Picsart")

    else:
        print(f"{RED}>{WHITE} Picsart | Ratelimit")
