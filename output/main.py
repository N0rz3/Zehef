from modules import account, rep, breached, pastebin
from lib.colors import *
from lib.objects import *
from lib.emails_gen import gen
from lib.name import *

from modules.possible_accounts.social import snapchat, tiktok

import re
from lib.utils import EMAIL_FORMAT


async def zehef(email: str):

    if re.match(EMAIL_FORMAT, email):
        v = TempPrint(f"{GREEN}[✔️] Email valid format!{WHITE}")
        v.TPrint()

    else:
        v = TempPrint(f"{RED}[❌] Email not valid format!{WHITE}")
        v.TPrint
        exit()

    print(f"""{BLUE}🐙 Reputation{WHITE}\n""")
    await rep.check_reputation(email)

    print(f"""{BLUE}🔎📂 Leak / Breach{WHITE}\n""")
    await breached.check(email)

    print(f"""\n\n{BLUE}🕶️  Dump Pastebin{WHITE}\n""")
    await pastebin.pastebin_dump(email)

    print(f"""{BLUE}\n\n💻 Possible accounts {WHITE}\n\n{YELLOW}👻 Snapchat :{WHITE}""")
    await snapchat.check(email)

    print(f"\n{YELLOW}📱 TikTok :{WHITE}")
    await tiktok.check(email)

    print(f"""\n\n{BLUE}😈 Account Checker{WHITE}\n""")
    await account.check_email(email)

    print(f"""\n\n\n{YELLOW}[?] 🔍 Generation of emails :{WHITE}\n""")
    await gen(email)
    print("\n")

    print(f"""\n{YELLOW}[?] 🤸🏻 Name search :{WHITE}""")
    await find_name(email)
