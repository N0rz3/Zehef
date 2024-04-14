import httpx
import requests

class Request:
    def __init__(self, url: str, headers=None, params=None, data=None):
        self.url = url
        self.head = headers
        self.params = params
        self.data = data

    async def get(self):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url=self.url, headers=self.head, params=self.params)
                return response

        except httpx.HTTPError:
            return httpx.Response(status_code=500)
        
    async def post(self):
        try:
            async with httpx.AsyncClient() as client:
                requests = await client.post(url=self.url, data=self.data, headers=self.head, params=self.params)

                return requests

        except httpx.HTTPError:
            return httpx.Response(status_code=500)

    def Session(self):
        try:
            session = requests.Session()
            return session
        
        except:
            pass