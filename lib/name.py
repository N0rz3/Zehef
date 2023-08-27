namess = {
    'johnny': 'john',
    'emily': 'emi',
    'michael': 'mike',
    'jessica': 'jess',
    'william': 'will',
    'alexandra': 'alex',
    'daniel': 'dan',
    'olivia': 'liv',
    'benjamin': 'ben',
    'sophia': 'sophie',
    'noe': 'nono',
    'jules': 'jul',
    'july': 'juju',
    'adam': 'ade',
    'adrian': 'adri',
    'aiden': 'aid',
    'alexander': 'alex',
    'amanda': 'mandy',
    'amelia': 'meli',
    'anna': 'annie',
    'anthony': 'tony',
    'ashley': 'ash',
    'aubrey': 'bree',
    'audrey': 'aud',
    'ava': 'avie',
    'brian': 'bri',
    'caleb': 'cay',
    'cameron': 'cam',
    'charles': 'charlie',
    'chloe': 'clo',
    'christopher': 'chris',
    'claire': 'clai',
    'david': 'dave',
    'dylan': 'dyl',
    'elijah': 'eli',
    'ella': 'elle',
    'ethan': 'eth',
    'eva': 'eve',
    'evan': 'ev',
    'grace': 'gracie',
    'gabriel': 'gabi',
    'hannah': 'han',
    'harrison': 'harry',
    'henry': 'hank',
    'isabella': 'bella',
    'isaac': 'ike',
    'jack': 'jackie',
    'jacob': 'jake',
    'jackson': 'jack',
    'james': 'jimmy',
    'jayden': 'jay',
    'jennifer': 'jen',
    'jeremy': 'jerry',
    'johnny': 'jon',
    'joseph': 'joe',
    'julia': 'jules',
    'justin': 'jay',
    'katherine': 'kat',
    'kevin': 'vin',
    'lauren': 'laurie',
    'liam': 'lee',
    'lillian': 'lily',
    'lily': 'lils',
    'lucas': 'luke',
    'lucy': 'lulu',
    'mason': 'mace',
    'matthew': 'matt',
    'mia': 'mimi',
    'nathan': 'nate',
    'nathaniel': 'nathan',
    'natalie': 'nat',
    'nicholas': 'nick',
    'noah' or 'noa': 'nono',
    'oliver': 'oliv',
    'owen': 'ow',
    'peter': 'pete',
    'rachel': 'rach',
    'rebecca': 'becky',
    'richard': 'ricky',
    'robert': 'rob',
    'ryan': 'ry',
    'samuel': 'samy',
    'samantha': 'sam',
    'sebastian': 'seb',
    'sophie': 'soso',
    'steven': 'steve',
    'thomas': 'tommy',
    'victoria': 'vicky',
    'william': 'willie',
    'zachary': 'zac',
    'neo': 'neyoo',
    'tom': 'tomtrack',
    'tom': 'trax',
    'philippe': 'fifi',
    'phoebe': 'bee',
    'brandon': 'brad',
    'florian': 'flo'
}

from .objects import *
import re

async def find_name(email: str):
    emailUniqueId = str(email.split("@")[0])
    # common delimeters for usernames
    usernameList = re.split(r"\-|\_|\.", emailUniqueId)
    founds = 0
    attempts = 0

    TempPrint(f"\n[+] 🐝 Search for a potential name...").TPrint()
    for fname, pseudo in namess.items():
        attempts += 1
        if fname in usernameList or pseudo in usernameList:
            founds += 1
            print("\n[+] Potential name found ~= " +  fname)

    if founds == 0:
        print("\n[-] No potential names found in this email address.")
