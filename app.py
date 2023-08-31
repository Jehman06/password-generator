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
        
@app.route("/", methods=["GET", "POST"])
def password_generator():
    if request.method == "POST":
        try:
            pwd_length = int(request.form["length"])
            if pwd_length <= 0:
                raise ValueError("Password length must be a positive integer.")

            password = generate_password(pwd_length)
            return render_template("index.html", password=password)
        except ValueError as e:
            return render_template("index.html", error=str(e))

    return render_template("index.html", password="")

if __name__ == "__main__":
    app.run(debug=True)