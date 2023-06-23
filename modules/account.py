"""
holehe => https://github.com/megadose/holehe
license holehe => https://www.gnu.org/licenses/gpl-3.0.fr.html
holehe owner => https://github.com/megadose
"""
from holehe.modules.company.aboutme import aboutme
from holehe.modules.shopping.amazon import amazon
from holehe.modules.social_media.bitmoji import bitmoji
from holehe.modules.sport.bodybuilding import bodybuilding
from holehe.modules.shopping.deliveroo import deliveroo
from holehe.modules.social_media.discord import discord
from holehe.modules.programing.github import github
from holehe.modules.mails.google import google
from holehe.modules.cms.gravatar import gravatar
from holehe.modules.social_media.instagram import instagram
from holehe.modules.mails.laposte import laposte
from holehe.modules.products.nike import nike
from holehe.modules.social_media.pinterest import pinterest
from holehe.modules.porn.pornhub import pornhub
from holehe.modules.mails.protonmail import protonmail
from holehe.modules.porn.redtube import redtube
from holehe.modules.music.smule import smule
from holehe.modules.music.spotify import spotify
from holehe.modules.social_media.twitter import twitter
from holehe.modules.payment.venmo import venmo
from holehe.modules.cms.wordpress import wordpress
from holehe.modules.porn.xnxx import xnxx
from holehe.modules.porn.xvideos import xvideos
from holehe.modules.mails.yahoo import yahoo


from lib.colors import *
import httpx
import datetime
import asyncio

"""
patch n°1 (SSL certificate) (test n°1)
"""

import ssl # patch for luted against error SSL 
ssl_context = ssl.create_default_context()
ssl_context.options |= ssl.OP_NO_SSLv2
ssl_context.options |= ssl.OP_NO_SSLv3
ssl_context.options |= ssl.OP_NO_TLSv1
ssl_context.options |= ssl.OP_NO_TLSv1_1

async def check_email(email: str):
    """
    Asynchrone function for checking if the email is linked to an account.
    Function works with holehe.

    List of all functions:
        - run_module(module, client): This function is used to run the holehe modules.
        
    Asynchrone HTTP client: This client serves to run the given module.
    """

    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    exist = []

    async def run_module(module, client):
        out = []
        try:
            await module(email, client, out)
        except httpx.ConnectError:
            pass
        exist.append(out)

    async with httpx.AsyncClient(verify=ssl_context) as client:
        tasks = []
        for module in [
            bitmoji, discord, instagram, pinterest, twitter, github, spotify, smule,
            google, protonmail, yahoo, laposte, amazon, deliveroo, pornhub, redtube,
            xnxx, xvideos, gravatar, wordpress, venmo, aboutme, nike, bodybuilding
        ]:
            tasks.append(run_module(module, client))

        await asyncio.gather(*tasks)

    resultCount = 0
    if exist:
        for result in exist:
            try:
                if result[0]['exists']:
                    print(f"[{GREEN}{date}{WHITE}] {GREEN}{result[0]['name'].upper()}{WHITE}")
                    resultCount += 1
            except:
                pass
    if resultCount == 0:
        print(f"{RED}[-]{WHITE} {RED}No related accounts were found!{WHITE}\n")
