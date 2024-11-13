import random
import re
from .colors import *

class Email_Gen:
    def __init__(self, email: str) -> None:
        self.e = email
        self.a_s = []  
        self.domains = [
            "gmail.com",
            "yahoo.com",
            "hotmail.com",
            "outlook.fr",
            "outlook.com",
            "aol.com",
            "icloud.com",
            "mail.com",
            "protonmail.com",
            "zoho.com",
            "gmx.com",
            "yandex.com",
            "tutanota.com",
            "mail.ru",
            "live.com",
            "fastmail.com",
        ]
        self.caract = [
            '!', 
            '?', 
            '$', 
            '#'
        ]

    def generate_email(self):
        random_domain = random.choice(self.domains)
        choice = lambda x: random.random() < x 
        name = self.e.split('@')[0] 
        special_char = random.choice(self.caract) if choice(0.3) else ''
        random_number = random.randint(100, 999) if choice(0.2) else ''

        if choice(0.3):
            name = re.sub(r'\d+', '', name) 

        if choice(0.4):
            name = name.replace('_', '').replace('.', '')

        if choice(0.3):
            name = str(name.lower()).replace('o', '0').replace('a', '4').replace('e', '3') 
        
        email = f"{name}{special_char}{random_number}@{random_domain}"
        return email

    def printer(self):
        num_emails = random.randint(5, 20) 

        emails = [self.generate_email() for _ in range(num_emails)]

        print(f"{GREEN}>{WHITE} {num_emails} Potentials emails generated !\n")

        for email in emails:
            if email in self.a_s:
                print(email + f" >{CYAN} Already shown{WHITE}")

            else:
                print(email)
                self.a_s.append(email)