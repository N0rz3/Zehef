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
        except httpx.HTTPError as e:
            print(f"HTTP error occurred: {e}")
            return httpx.Response(status_code=500)
        except Exception as e:
            print(f"An error occurred: {e}")
            return httpx.Response(status_code=500)

    async def post(self):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(url=self.url, data=self.data, headers=self.head, params=self.params)
                return response
        except httpx.HTTPError as e:
            print(f"HTTP error occurred: {e}")
            return httpx.Response(status_code=500)
        except Exception as e:
            print(f"An error occurred: {e}")
            return httpx.Response(status_code=500)

    def Session(self):
        try:
            session = requests.Session()
            return session
        except Exception as e:
            print(f"An error occurred while creating a session: {e}")
            return None
