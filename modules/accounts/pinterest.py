from lib.Requests import Request
from lib.colors import *

async def pinterest(target: str):

    params={
        "source_url": "/",
        "data": '{"options": {"email": "'+ target +'"}, "context": {}}'
    }

    r = await Request("https://www.pinterest.fr/resource/EmailExistsResource/get/", params=params).get()

    try:
        if r.json()["resource_response"]["data"]:
            print(f"{GREEN}>{WHITE} Pinterest")

        else:
            print(f"{RED}>{WHITE} Pinterest")

    
    except:
        print(f"{RED}>{WHITE} Pinterest")