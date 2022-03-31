from distutils.log import debug
from smtpd import DebuggingServer
from flask import Flask, render_template
from random import randint
import datetime
import requests

AGE_API="https://api.agify.io/"
GENDER_API="https://api.genderize.io/"

app = Flask(__name__)

@app.route("/")
def home():
    random_number = randint(1, 10)
    year = datetime.datetime.today().year

    return render_template("index.html", num=random_number, year=year, name="Daniel Navarrete")

@app.route("/guess/<name>")
def guess(name):
    name = name.title()
    params = {
        "name": name,
    }
    response = requests.get(AGE_API, params=params)
    response = response.json()
    age = response["age"]
    response = requests.get(GENDER_API, params=params)
    response = response.json()
    gender = response["gender"]
    return render_template("guess.html", name=name, gender=gender, age=age)

@app.route("/blog/<num>")
def blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    posts = response.json()
    return render_template("blog.html", posts=posts, num=num)

if __name__ == "__main__":
    app.run(debug=True)