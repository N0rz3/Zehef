"""
original code => https://github.com/KanekiWeb/Email-Osint/blob/main/modules/PastebinDump.py
"""
from ScrapeSearchEngine.SearchEngine import Google
from lib.colors import *
from lib.request import *

async def pastebin_check(i, email):
	try:
		link = str(i).replace("https://pastebin.com/","https://pastebin.com/raw/")
		r = Requests(link)
		data = await r.sender()

		if email.lower() in data.text.lower() or email in data.text or email.upper() in data.text.upper():
			print(RED+"[!] "+link)

	except:
		print("[!] Your adresse IP has banned, retry tomorrow or change your ip.".replace('!',RED+'!'+WHITE))

async def pastebin_dump(email):

	search = ("site:pastebin.com \"{}\"".format(email))
	try:
		googleText, googleLink = Google(search=search, userAgent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Safari/537.36")

		for i in googleLink:
			await pastebin_check(i, email)

	except:
		print("[!] 🤔 Error.".replace('!',RED+'!'+WHITE))