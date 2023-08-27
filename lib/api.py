"""
api used
"""
def reputation(email) -> None:
    return "http://api.eva.pingutil.com/email?email={}".format(email)
