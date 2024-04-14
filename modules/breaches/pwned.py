import pwnedpasswords
from lib.colors import *

def pwned(target: str):
    pass_check = pwnedpasswords.check(target)

    if pass_check:
        print(f"{RED}>{WHITE} Status : PWNED ~ password")
    else: 
        print(f"{GREEN}>{WHITE} Status : SAFE ~ password")