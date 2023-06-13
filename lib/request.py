import httpx    

class Requests: # class for send the requests
    """
    Requests function with httpx

    Parameters of the requests in __init__(url, headers, params)
    Asynchrone function: sender() - for sending the requests

    An asynchrone HTTP client is created to send all requests with the provided headers and parameters.
    """

    def __init__(self, url: str, headers=None, params=None):
        """
        Parameters:
            url (str)      : url used for send a requests
            headers (None) : headers used if desired 
            params (None)  : parameters used if desired 
        """

        self.url = url
        self.headers = headers
        self.params = params

    async def sender(self):
        try:
            async with httpx.AsyncClient() as client:
                r = await client.get(self.url, headers=self.headers, params=self.params)
                return r

        except httpx.HTTPError:
            print("[-] Failed connection.")