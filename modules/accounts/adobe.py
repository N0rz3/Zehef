from lib.colors import *
from lib.Requests import *

async def adobe(target: str):
    data = {
        "username": target,
        "usernameType": "EMAIL"
    }

    headers = {
        'x-ims-clientid': 'homepage_milo',
        'content-type': 'application/json'
    }

    r = await Request("https://auth.services.adobe.com/signin/v2/users/accounts", headers=headers, json=data).post()

    try:
        if r.json()[0]['authenticationMethods']:
            print(f"{GREEN}>{WHITE} Adobe")

        else:
            print(f"{RED}>{WHITE} Adobe")

    except:
        print(f"{RED}>{WHITE} Adobe")