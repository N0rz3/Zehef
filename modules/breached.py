import pwnedpasswords
from lib.colors import *


async def check(email: str):
    """
    Asynchrone function for check if email has leaked or breached with pwnedpasswords
    """
    pass_check = pwnedpasswords.check(email)

    if pass_check:
        print(f"EMAIL Status : {RED}[BREACHED]{WHITE}")
    else:
        print(f"EMAIL Status : {GREEN}[SAFE]{WHITE}")