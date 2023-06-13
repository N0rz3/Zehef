import sys, asyncio

def version():
    v = sys.version_info
    if (v < (3, 10)):
        print("[-] Zehef only works with Python 3.10+.")
        exit("[+] Go install the most recent version of python -> https://www.python.org/downloads/")

    from lib import CLI
    loop = asyncio.get_event_loop()
    loop.run_until_complete(CLI.parser())