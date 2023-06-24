"""
original code => https://github.com/KanekiWeb/Email-Osint/blob/main/modules/PastebinDump.py
"""
from ScrapeSearchEngine.SearchEngine import Google
from lib.colors import *
from lib.request import *
from lib.objects import *

import asyncio

async def pastebin_check(i, email, result_links):
    try:
        link = str(i).replace("https://pastebin.com/", "https://pastebin.com/raw/")
        r = Requests(link)
        data = await r.sender()

        if email.lower() in data.text.lower() or email in data.text or email.upper() in data.text.upper():
            result_links.append(link)

    except:
        print("[!] Your IP address has been banned. Retry tomorrow or change your IP.".replace('!', RED + '!' + WHITE))

async def pastebin_dump(email):
    search = ("site:pastebin.com \"{}\"".format(email))
    try:
        googleText, googleLink = Google(search=search, userAgent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Safari/537.36")
        scraping_msg = TempPrint("[+] 😴 Dumping...")
        scraping_msg.TPrint()

        result_links = []

        tasks = []
        for i in googleLink:
            task = pastebin_check(i, email, result_links)
            tasks.append(task)

        await asyncio.gather(*tasks)

        for link in result_links:
            print(RED + "[!] " + link + WHITE)

    except:
        print("[!] 🤔 Error.".replace('!', RED + '!' + WHITE))
