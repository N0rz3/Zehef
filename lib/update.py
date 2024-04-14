import json
from .Requests import Request
from .colors import *

class Version_Checker:
    async def checker():
        with open('config.json', "+r", encoding='utf-8') as file:
            reader = json.loads(file.read())

        version = reader['version']['number']
        name = reader['version']['name']

        print(f"[ {RED}{name} version{WHITE} ]")

        r = await Request("https://raw.githubusercontent.com/N0rz3/Zehef/master/config.json").get()

        conf = json.loads(r.text)

        current_version = conf['version']['number']

        if version == current_version:
            print(f"\n{GREEN}>{WHITE} 🎊 You're up to date ! ~ v{current_version}\n")

        else: 
            print(f"\n{RED}>{WHITE} 🔥 The new version {current_version} is available\n")