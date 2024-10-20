from lib.Requests import Request
from lib.colors import *

async def strava(target: str):

    params = {'email': target}

    req = await Request(f"https://www.strava.com/frontend/athletes/email_unique", params=params).get()

    try:
        if "false" in req.text:
            print(f"{GREEN}>{WHITE} Strava")

        elif "true" in req.text:
            print(f"{RED}>{WHITE} Strava")

        else:
            print(f"{RED}>{WHITE} Strava")
            
    except:
        print(f"{RED}>{WHITE} Strava")
