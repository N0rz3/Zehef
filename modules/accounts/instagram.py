from lib.Requests import Request
from lib.colors import *

async def instagram(target: str):
    req = await Request("https://www.instagram.com/accounts/emailsignup/").get()

    try:
        csrf_token = req.cookies.get('csrftoken')
    except:
        print(f"{RED}>{WHITE} Instagram / Csrftoken not found")
        pass

    data = {
        'email': target,
        'first_name': '',
        'username': '',
        'opt_into_one_tap': False
    }

    r = await Request("https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/", headers={'x-csrftoken': csrf_token}, data=data).post()
    
    try:
        code = r.json().get('errors', {}).get('email', [{}])[0].get('code')

        if code == 'email_is_taken':
            print(f"{GREEN}>{WHITE} Instagram")
        else:
            print(f"{RED}>{WHITE} Instagram")

    except (KeyError, IndexError) as e:
        print(f"{RED}>{WHITE} Instagram error: {str(e)}")

    except Exception as e:
        print(f"{RED}>{WHITE} Error: {str(e)}")
