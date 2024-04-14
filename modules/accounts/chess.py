from lib.Requests import Request
from lib.colors import *

async def chess(target: str):

    r = await Request(f"https://www.chess.com/callback/email/available?email={target}").post()

    try:
        if r.json()['isEmailAvailable'] == True:
            print(f"{RED}>{WHITE} Chess")

        elif r.json()['isEmailAvailable'] == False:
            print(f"{GREEN}>{WHITE} Chess")

        else:
            print(f"{RED}>{WHITE} Chess")

    except:
        pass