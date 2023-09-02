import secrets
import string
from flask import Flask, render_template, request, jsonify

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
        
def generate_new_password(pwd_length):
    return generate_password(pwd_length)
        
@app.route("/", methods=["GET", "POST"])
def password_generator():
    if request.method == "POST":
        try:
            pwd_length = int(request.form["length"])
            if pwd_length <= 0:
                raise ValueError("Password length must be a positive integer.")
            elif pwd_length > 20:
                raise ValueError("Password length cannot be more than 20.")

            password = generate_password(pwd_length)
            return render_template("index.html", password=password)
        except ValueError as e:
            return render_template("index.html", error=str(e))

    return render_template("index.html", password="")

@app.route("/generate-new-password", methods=["POST"])
def generate_new_password_route():
    try:
        pwd_length = 12  # Update with your desired password length
        password = generate_new_password(pwd_length)  # Generate a new password
        return jsonify({'password': password})
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return an error response if an exception occurs

if __name__ == "__main__":
    app.run(debug=True)