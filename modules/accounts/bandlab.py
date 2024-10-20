from lib.Requests import Request
from lib.colors import *

async def bandlab(target: str):

    r = await Request(f"https://www.bandlab.com/api/v1.3/validation/user", params={'email': target}).get()

    if r.json()['isValid']:
        if r.json()['isAvailable'] == False:
            print(f"{GREEN}>{WHITE} Bandlab")

        else:
            print(f"{RED}>{WHITE} Bandlab")

    else:
        print(f"{RED}>{WHITE} Bandlab")