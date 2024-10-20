from lib.Requests import Request
from lib.colors import *
import re

async def flickr(target: str):
    count = 0
    r = await Request("https://www.flickr.com/").get()

    key_pattern = r'[a-f0-9]{32}'
    keys = re.findall(key_pattern, r.text)

    api_keys = set(keys)

    if api_keys:
        for key in api_keys:
            api = "https://api.flickr.com/services/rest"

            params = {
                'username': target,
                'exact': 0,
                'extras': 'path_alias%2Crev_ignored%2Crev_contacts%2Cis_pro%2Cicon_urls%2Clocation%2Crev_contact_count%2Cuse_vespa%2Cdate_joined',
                'per_page': 5,
                'page': 0,
                'show_more': 1,
                'perPage': 50,
                'loadFullContact': 1,
                'viewerNSID': None,
                'method': 'flickr.people.search',
                'api_key': key,
                'format': 'json',
                'hermes': 1,
                'hermesClient': 1,
                'nojsoncallback': 1
            }

            r = await Request(api, params=params).get()

            try:
                data = r.json()['people']['person'][0]

                print(f"{GREEN}>{WHITE} Flickr")
                count += 1
                print(f"  ├──> Username : {data['username']}")

                name = data['realname']
                if name != '':
                    print(f"  ├──> Name : {data['realname']}")
                else:
                    pass
                print(f"  ├──> Id : {data['dbid']}")
                print(f"  └──> Account : {CYAN}https://www.flickr.com/people/{data['nsid']}/{WHITE}")

                break

            except:
                continue

    else:
        pass

    if count == 0:
        print(f"{RED}>{WHITE} Flickr")

    else:
        pass
