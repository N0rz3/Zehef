from modules import account, rep, breached
from lib.colors import *

from modules.possible_accounts.social import snapchat, tiktok

import re
from lib.utils import EMAIL_FORMAT


async def zehef(email: str):

    if re.match(EMAIL_FORMAT, email):
        print(f"{GREEN}[✔️  ] Email valid format!{WHITE}\n\n")
    else:
        print(f"{RED}[❌ ] Email not valid format!{WHITE}")
        exit()

    print(f"""{BLUE}🐙 Reputation{WHITE}\n""")
    await rep.check_reputation(email)

    print(f"""{BLUE}🔎📂 Leak / Breach{WHITE}\n""")
    await breached.check(email)

    print(f"""{BLUE}\n\n💻 Possible accounts {WHITE}\n\n{YELLOW}👻 Snapchat :{WHITE}""")
    await snapchat.check(email)

    print(f"\n{YELLOW}📱 TikTok :{WHITE}")
    await tiktok.check(email)


    print(f"""\n\n{BLUE}😈 Account Checker{WHITE}\n""")
    await account.check_email(email)