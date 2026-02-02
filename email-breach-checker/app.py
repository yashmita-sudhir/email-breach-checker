# app.py

from flask import Flask, render_template, request
from breach_checker import check_email

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        email = request.form.get("email", "").strip()
        result = check_email(email)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

