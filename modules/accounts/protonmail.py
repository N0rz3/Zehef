from lib.Requests import Request
from lib.colors import *
from datetime import datetime
import re

async def protonmail(target: str):

    target_domain = target.split('@')[1]
    proton_domains = ['pm.me', 'proton.me', 'protonmail.com', 'protonmail.ch']

    if target_domain in proton_domains:

        api = f"https://api.protonmail.ch/pks/lookup?op=index&search={target}"

        r = await Request(api).get()

        match = re.search(r'\b\d{10}\b', r.text)

        if match:
            timestamp = int(match.group())
            date_of_creation = datetime.fromtimestamp(timestamp)

            print(f"{GREEN}>{WHITE} Protonmail")
            print(f"  └──> Created on : {date_of_creation}")

        else:
            print(f"{RED}>{WHITE} Protonmail")

    else:
        print(f"{RED}>{WHITE} Protonmail")