from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "pascha"

@app.route("/hello")
def index():
    flash("Was ist Ihr Name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form["name_input"]) + ", bald haben Sie Ihren Pass.")
    return render_template("index.html")
