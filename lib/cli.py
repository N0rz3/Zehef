import argparse 
import re
from .colors import *
from .update import Version_Checker
from modules.accounts.twitter import x
from modules.accounts.gravatar import gravatar
from modules.accounts.spotify import spotify
from modules.accounts.duolingo import duolingo
from modules.accounts.pinterest import pinterest
from modules.accounts.github import github
from modules.accounts.strava import strava
from modules.accounts.pornhub import pornhub
from modules.accounts.chess import chess
from modules.accounts.deezer import deezer
from modules.accounts.imgur import imgur
from modules.accounts.instagram import instagram
from modules.breaches.pastedumper import Pastebin_Dumper
from modules.breaches.pwned import pwned
from .emails_gen import Email_Gen

async def parser():
    await Version_Checker.checker()

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "email",
        nargs="?",
        type=str,
        default=None,
        help="Search informations on email (breaches, pastes, accounts ...)"
    )

    args = parser.parse_args()

    if args.email:
        target = args.email

        EMAIL_REGEX = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$'

        if re.match(EMAIL_REGEX, target):
            print(f"\n{PURPLE}📁 Leaks{WHITE}\n")

            pwned(target)

            print()

            await Pastebin_Dumper(target).paste_check()

            print(f"\n{YELLOW}🎭 Accounts{WHITE}\n")
            
            await chess(target)
            deezer(target)
            await duolingo(target)
            await github(target)
            await gravatar(target)
            imgur(target)
            await instagram(target)
            await pinterest(target)
            pornhub(target)
            await spotify(target)
            await strava(target)
            await x(target)
            

            print(f"\n{PINK}📧 Email generation{WHITE}\n")
            Email_Gen(target).printer()

        else:
            exit(f"{RED}>{WHITE} The target isn't an email.")

    else:
        pass