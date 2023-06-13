"""
All api used
"""
def emailrep(email) -> None:
    return "https://emailrep.io/{}".format(email)

def verify_email(email) -> None:
    return "https://verify-email.org/home/verify-as-guest/{}".format(email)