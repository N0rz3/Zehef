from lib.Requests import Request
from lib.colors import *

async def duolingo(target: str):

    r = await Request(f"https://www.duolingo.com/2017-06-30/users", params={'email': target}).get()

    try:
        if """{"users":[]}""" in r.text:
            print(f"{RED}>{WHITE} Duolingo")

        else:
            valid = r.json()['users'][0]['username']
            
            print(f"{GREEN}>{WHITE} Duolingo")

    except:
        print(f"{RED}>{WHITE} Duolingo")