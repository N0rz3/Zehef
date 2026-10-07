from lib.Requests import Request
from lib.colors import *

async def picsart(target: str):

    params = {
        'email_encoded': 1,
        'emails': target
    }

    try:
        r = await Request("https://api.picsart.com/users/email/existence", params=params).get()
        data = r.json()
    except Exception:
        return

    if data.get('status') == 'success':

        if data.get('response'):
            print(f"{GREEN}>{WHITE} Picsart")

        else:
            print(f"{RED}>{WHITE} Picsart")

    else:
        print(f"{RED}>{WHITE} Picsart | Ratelimit")
