from flask import Flask, render_template
import requests
from datetime import datetime as dt


app = Flask(__name__)
current_year = dt.now().strftime("%Y")


def blogs():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    res = requests.get(url)
    res.raise_for_status()
    blog_data = res.json()
    return blog_data


@app.route('/')
def home():
    blog_data = blogs()
    return render_template("index.html", posts=blog_data)


@app.route('/posts/<num>')
def get_posts(num):
    num = int(num)
    blog_data = blogs()
    for blog in blog_data:
        if blog["id"] == num:
            blog_title = blog["title"]
            blog_body = blog["body"]
    return render_template("post.html", title=blog_title, body=blog_body)


if __name__ == "__main__":
    app.run(debug=True)
