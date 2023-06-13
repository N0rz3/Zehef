import argparse

from lib import headers
from output import main


async def parser():
    """
    Menu format : cli 

    - this function serves to used commands with argparse
    - (asynchrone function)
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "email",
        nargs="?",
        type=str,
        default=None,
        help="Search information on target email with API(s), holehe, and others..."
    )

    args = parser.parse_args()

    if args.email:
        print(headers.h1)
        email = args.email
        await main.zehef(email)

    else:
        print(headers.h2)