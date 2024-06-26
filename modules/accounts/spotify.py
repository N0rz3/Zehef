from lib.Requests import Request
from lib.colors import *

async def spotify(target: str):

    r = await Request(f"https://spclient.wg.spotify.com/signup/public/v1/account?validate=1&email={target}").get()

    try:
        if r.json()['status'] == 20:
            print(f"{GREEN}>{WHITE} Spotify")

        else:
            print(f"{RED}>{WHITE} Spotify")

    except:
        print(f"{RED}>{WHITE} Spotify")