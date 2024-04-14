from lib.Requests import Request
from lib.colors import *

async def instagram(target: str):

    req = await Request("https://www.instagram.com/accounts/emailsignup/").get()

    csrf_token = req.cookies['csrftoken']

    data = {
        'email': target,
        'first_name': '',
        'username': '',
        'opt_into_one_tap': False
    }

    r = await Request("https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/", headers={'x-csrftoken': csrf_token}, data=data).post()

    try:
        code = r.json()['errors']['email'][0]['code']

        if code == 'email_is_taken':
            print(f"{GREEN}>{WHITE} Instagram")

        else:
            print(f"{RED}>{WHITE} Instagram")

    except:
        print(f"{RED}>{WHITE} Instagram")