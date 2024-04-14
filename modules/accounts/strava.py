from lib.Requests import Request
from lib.colors import *

async def strava(target: str):

    req = await Request(f"https://www.strava.com/athletes/email_unique?email={target}").get()

    try:
        if "false" in req.text:
            print(f"{GREEN}>{WHITE} Strava")

        elif "true" in req.text:
            print(f"{RED}>{WHITE} Strava")

        else:
            print(f"{RED}>{WHITE} Strava")
            
    except:
        pass