from flask import Flask, render_template
import requests

app = Flask(__name__)

res = requests.get("https://api.jsonbin.io/v3/qs/6545301a0574da7622c1a0f9")
res.raise_for_status()
data = res.json()["record"]


@app.route('/')
def home():
    return render_template("index.html", posts=data)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/post/<num>')
def post(num):
    data_list = data
    num = int(num)
    for post in data_list:
        if post["id"] == num:
            post_data = data_list[num - 1]
            image_url = post_data["image_url"]
            image_alt = post_data["image_alt"]
            title = post_data["title"]
            author = post_data["author"]
            date = post_data["date"]
            body = post_data["body"]
            subtitle = post_data["subtitle"]

    return render_template("post.html", title=title, author=author, date=date, body=body, subtitle=subtitle, image_url=image_url, image_alt=image_alt)


if __name__ == "__main__":
    app.run(debug=True)
