import time

class TempPrint:
    """
    Function for print a text for a turn of time
    """
    def __init__(self, 
                message:str,
                temp: int = 3,
                ):
        self.msg = message
        self.temp = temp

    def TPrint(self):
        print(self.msg, end="", flush=True)
        time.sleep(self.temp)
        print("\r" + " " * len(self.msg) + "\r", end="", flush=True)
