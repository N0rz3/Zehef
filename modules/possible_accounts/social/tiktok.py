from lib.request import *
from lib.colors import *

async def check(email: str):
    """
    Asynchrone function for check the name below several formats in tiktok

    list function:
        - decomp()     : decompil email for give the name and remove the domain
        - variations() : check the name result by decomp() in the several formats

    check the code of requests for return if a account exist with the name formated

    Parameter:
        email (str) : email target

    Return:
        str : all urls found
    """

    def decomp():
        """
        Return:
            name (str) : name behind domain name exemple => (example@example.com) convert in => (example)
        """

        name = email.split("@")[0]
        return name


    def variations():
        """
        Return:
            upp, low, num, lett, a, no_num (str) : its a variations of name found with the function decomp()
        """
        name = decomp()

        upp = name.upper()
        low = name.lower()
        num = name.replace("1", "i").replace("3", "e").replace("4", "a").replace("8", "b").replace("0", "o")
        lett = name.replace("i", "1").replace("e", "3").replace("a", "4").replace("b", "8").replace("o", "0")
        a = name.replace(".", "").replace("-", "").replace("_", "")
        no_num = name.replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "").replace("0", "")

        return upp, low, num, lett, a, no_num

    shown_urls = set()
    name_vars = variations()

    for var in name_vars:
        URL = "https://www.tiktok.com/@{}".format(var)
        r = Requests(URL)
        response = await r.sender()

        if response.status_code == 200:
            if URL in shown_urls:
                print(GREEN + "[+] " + URL + BLACK + " [Already shown]" + WHITE)
                continue
            else:
                shown_urls.add(URL)
                print(GREEN + "[+] " + URL + WHITE)
        else:
            if URL in shown_urls:
                print(RED + "[-] " + URL + BLACK + " [Already shown]" + WHITE)
                continue
            else:
                shown_urls.add(URL)
                print(RED + "[-] " + URL + WHITE)
