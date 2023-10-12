from flask import Flask, render_template
from datetime import datetime as dt
import requests

app = Flask(__name__)


def get_query(url, name):
    res = requests.get(url + name)
    res.raise_for_status()
    data = res.json()
    return data


current_year = dt.now().strftime("%Y")
MY_NAME = "Nicholas"


@app.route('/')
def home():
    return render_template('index.html', year=current_year, my_name=MY_NAME)


@app.route('/guess/<name>')
def guess(name):
    name = name.capitalize()
    age = get_query(url="https://api.agify.io?name=", name=name)["age"]
    gender = get_query(url="https://api.genderize.io?name=",
                       name=name)["gender"]

    return render_template('guess.html', age=age, gender=gender, name=name)


@app.route('/blog')
def get_blog():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    res = requests.get(url)
    res.raise_for_status()
    blog_data = res.json()
    return render_template("blog.html", posts=blog_data)


if __name__ == '__main__':
    app.run(debug=True)
