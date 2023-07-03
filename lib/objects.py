import time

class TempPrint:
    """
    Function for printing a text for a certain period of time
    """
    def __init__(self, message: str, temp: int = 3):
        self.msg = message.rstrip()
        self.temp = temp

    def TPrint(self):
        print(self.msg, end="", flush=True)
        time.sleep(self.temp)
        print("\r" + " " * (len(self.msg) + 1) + "\r", end="", flush=True)
