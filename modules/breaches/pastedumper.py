import random
from bs4 import BeautifulSoup
from lib.Requests import Request
from lib.colors import *

class Pastebin_Dumper:
    def __init__(self, target: str) -> None:
        self.target = target
        self.dork = f"site:pastebin.com \"{target}\""
        self.numbs = 0
        self.links = []
        self.ua = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/123.0.6312.52 Mobile/15E148 Safari/604.1"
        ]

    async def google_dorks_scraper(self):
        r = await Request(f"https://www.google.com/search?q={self.dork}", headers={"User-Agent": random.choice(self.ua)}).get()

        soup = BeautifulSoup(r.text, 'html.parser')
        search_results = soup.find_all('div', class_='tF2Cxc')

        for result in search_results:
            link = result.find('a')['href']

            self.links.append(link)

    async def paste_check(self):
        await self.google_dorks_scraper()

        for link in self.links:
            link_ = str(link).replace('https://pastebin.com/', 'https://pastebin.com/raw/')

            r = await Request(link_).get()

            if str(self.target).lower() in r.text.lower():
                print(f"{RED}>{WHITE} {link}")
                self.numbs += 1

            else:
                continue

        if self.numbs == 0:
            print(f"{GREEN}>{WHITE} No paste found.")
