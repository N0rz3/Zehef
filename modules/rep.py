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

        r = Requests(api.emailrep(email))
        resp = await r.sender()
        js = json.loads(resp.text)

        if js['details']['malicious_activity'] == True:
            print(f"\n[{RED}{date}{WHITE}] {RED}Malicious Activity{WHITE}")
        else:
            print(f"[{GREEN}{date}{WHITE}] {GREEN}No Malicious Activity{WHITE}")

        if js['details']['credentials_leaked'] == True:
            print(f"[{RED}{date}{WHITE}] {RED}Credentials Leaked{WHITE}")
        else:
            print(f"[{GREEN}{date}{WHITE}] {GREEN}No Credentials Leaked{WHITE}")

        if js['details']['data_breach'] == True:
            print(f"[{RED}{date}{WHITE}] {RED}Data Breach{WHITE}")
        else:
            print(f"[{GREEN}{date}{WHITE}] {GREEN}No Data Breach{WHITE}")

        if js['details']['spam'] == True:
            print(f"[{RED}{date}{WHITE}] {RED}Spammer{WHITE}")
        else:
            print(f"[{GREEN}{date}{WHITE}] {GREEN}No Spammer{WHITE}")

        if js['details']['spoofable'] == True:
            print(f"[{RED}{date}{WHITE}] {RED}Spoofable{WHITE}")
        else:
            print(f"[{GREEN}{date}{WHITE}] {GREEN}No Spoofable{WHITE}")

        if js['details']['days_since_domain_creation'] == True:
            print(f"[{GREEN}{date}{WHITE}] {GREEN}Day Since Domain Creation: {js['details']['days_since_domain_creation']}")

        print(f"\n[{YELLOW}{date}{WHITE}] Reputation => {js['reputation']}{WHITE}")
        print(f"[{YELLOW}{date}{WHITE}] Suspicious => {js['suspicious']}{WHITE}\n\n")
    except:
        print(f"[{date}] Error : Ratelimit, please change your ip.\n\n")