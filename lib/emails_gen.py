import random, string
from .objects import *
from .colors import *
from .domains import email_domains

async def gen(email: str):


    def decomp():
        name = email.split("@")[0]
        return name


    def variations():
        name = decomp()


        upp = name.upper() + "@" + random.choice(email_domains)
        low = name.lower() + "@" + random.choice(email_domains)
        num = (
            name.replace("1", "i")
            .replace("3", "e")
            .replace("4", "a")
            .replace("8", "b")
            .replace("0", "o") + "@" + random.choice(email_domains)
        )
        lett = (
            name.replace("i", "1")
            .replace("e", "3")
            .replace("a", "4")
            .replace("b", "8")
            .replace("o", "0") + "@" + random.choice(email_domains)
        )
        a = (
            name.replace(".", "")
            .replace("-", "")
            .replace("_", "") + "@" + random.choice(email_domains)
        )
        no_num = (
            name.replace("1", "")
            .replace("2", "")
            .replace("3", "")
            .replace("4", "")
            .replace("5", "")
            .replace("6", "")
            .replace("7", "")
            .replace("8", "")
            .replace("9", "")
            .replace("0", "") + "@" + random.choice(email_domains)
        )

        ett = (
            name.upper().replace("I", "1")
            .replace("E", "3")
            .replace("A", "4")
            .replace("B", "8")
            .replace("O", "0") + "@" + random.choice(email_domains)
        )

        dedede = name.join("$$")

        r = name + "".join(random.choices(string.digits + string.digits + string.digits + string.digits + string.digits + string.digits + string.digits)) + "@" + random.choice(email_domains)

        return upp, low, num, lett, a, no_num, ett, r

    var = variations()

    msg = TempPrint("[+] 🧠 Generation of variations of target email...", temp=3)
    msg.TPrint()

    list = []

    for v in var:

        if v in list:
            print(f"[+] {v} {BLACK}[Already shown]{WHITE}")
            continue
        else:
            print(f"[+] {v}")
            list.append(v)