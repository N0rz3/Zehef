import requests
from lib.colors import *

def imgur(target: str):

    r = requests.post("https://imgur.com/signin/ajax_email_available", data={'email': target})

    try:
        if r.json()['data']['available'] == True:
            print(f"{RED}>{WHITE} Imgur")

        elif r.json()['data']['available'] == False:
            print(f"{GREEN}>{WHITE} Imgur")

        else:
            print(f"{RED}>{WHITE} Imgur")

    except:
        pass