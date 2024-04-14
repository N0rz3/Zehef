from lib.Requests import Request
from lib.colors import *

def deezer(target: str):
    try:
        s = Request(url=None).Session()

        r = s.post("https://www.deezer.com/ajax/gw-light.php?method=deezer.getUserData&input=3&api_version=1.0&api_token=&cid=")
        token = r.json()['results']['checkForm']

        params = {
            'method': 'deezer.emailCheck',
            'input': 3,
            'api_version': 1.0,
            'api_token': token,
        }

        api = s.post(f"https://www.deezer.com/ajax/gw-light.php", params=params, data='{"EMAIL":"'+ target +'"}')

        if api.json()['results']['availability'] == True:
            print(f"{RED}>{WHITE} Deezer")

        elif api.json()['results']['availability'] == False:
            print(f"{GREEN}>{WHITE} Deezer")

        else:
            print(f"{RED}>{WHITE} Deezer")

        s.close()

    except:
        s.close()
        pass