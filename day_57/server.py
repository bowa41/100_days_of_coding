from flask import Flask, render_template
from datetime import date
import requests
# from functools import wraps
app = Flask(__name__)

@app.route("/")
def home():
    year = date.today().year
    return render_template("index.html", CURRENT_YEAR=year)

@app.route("/guess/<name>")
def guess_age_gender(name):
    year = date.today().year
    response1 = requests.get(url=f"https://api.agify.io?name={name}")
    data1 = response1.json()
    response2 = requests.get(url=f"https://api.genderize.io?name={name}")
    data2 = response2.json()
    return render_template("index2.html", name=name.title(), gender=data2["gender"],
                           age=data1["age"], CURRENT_YEAR=year)

@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response3 = requests.get(url=blog_url)
    all_posts = response3.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
