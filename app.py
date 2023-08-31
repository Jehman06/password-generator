import secrets
import string
from flask import Flask, render_template, request

app = Flask(__name__)

def generate_password(pwd_length):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars

    while True:
        pwd = ''.join(secrets.choice(alphabet) for _ in range(pwd_length))

        if (any(char in special_chars for char in pwd) and sum(char in digits for char in pwd) >= 2):
            return pwd
        
print(generate_password(15))