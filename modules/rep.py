import json, datetime

from lib.colors import *
from lib.request import *
from lib import api

async def check_reputation(email: str):
    """
    Asynchrone function for check the reputation of email give thanks to api
    
        - scraping of the result of the request to the api 
    """
    try:
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        r = Requests(api.reputation(email))
        resp = await r.sender()
        js = json.loads(resp.text)

        if js['data']['disposable'] == True:
            print(f"[{RED}{date}{WHITE}] {RED}Disposable{WHITE}")
        else:
            print(f"[{GREEN}{date}{WHITE}] {GREEN}No Disposable{WHITE}")

        if js['data']['deliverable'] == True:
            print(f"[{RED}{date}{WHITE}] {RED}Deliverable{WHITE}")
        else:
            print(f"[{GREEN}{date}{WHITE}] {GREEN}No Deliverable{WHITE}")

        if js['data']['spam'] == True:
            print(f"[{RED}{date}{WHITE}] {RED}Spammer{WHITE}")
        else:
            print(f"[{GREEN}{date}{WHITE}] {GREEN}No Spammer{WHITE}")

        if js['data']['spam'] == True:
            print(f"[{RED}{date}{WHITE}] {RED}Spammer{WHITE}")
        else:
            print(f"[{GREEN}{date}{WHITE}] {GREEN}No Spammer{WHITE}")

    except:
        print(f"[{date}] Error : Ratelimit, please change your ip.\n\n")
