from lib.Requests import Request
from lib.colors import *
import json
from datetime import datetime

class Cavalier:
    def __init__(self, email: str) -> None:
        self.email = email
        self.api = "https://cavalier.hudsonrock.com/api/json/v2/osint-tools/search-by-email"

    async def loader(self):
        response = await Request(self.api, headers={'api-key': 'ROCKHUDSONROCK'}, params={'email': self.email}).get()

        try:
            data = response.json()['stealers'][0]

            print(f"[{RED}HudsonRock{WHITE}] Email's result :")
            print("> Total service corporate :", data.get('total_corporate_services', '/'))
            print("> Total user services :", data.get('total_user_services', '/'))

            time_iso = data.get('date_compromised')

            t_datetime = datetime.fromisoformat(time_iso.replace("Z", "+00:00"))
            date = t_datetime.strftime("%Y-%m-%d %H:%M:%S")

            print("> Date compromised :", date)
            print("> Computer name :", data.get('computer_name', '/'))
            print("> Operating system :", data.get('operating_system', '/'))
            print("> Ip address :", data.get('ip', '/'))

            try:
                top_passwords = data.get('top_passwords', [])
                top_logins = data.get('top_logins', [])

                print("> Top passwords :", ', '.join(top_passwords))
                print("> Top logins :", ', '.join(top_logins))

            except:
                print("> Top passwords : /")
                print("> Top logins : /")

        except(KeyError, json.JSONDecodeError):
            print(f"[{RED}HudsonRock{WHITE}] Email Safe")