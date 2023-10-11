from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/images/<img>")
def images(img):
    return redirect(f"/static/images/{img}")


@app.route("/assets/css/<file>")
def css(file):
    return redirect(f"/static/assets/css/{file}")


@app.route("/assets/js/<file>")
def js(file):
    return redirect(f"/static/assets/js/{file}")


@app.route("/assets/sass/<file>")
def sass(file):
    return redirect(f"/static/assets/sass/{file}")


@app.route("/assets/webfonts/<file>")
def webfonts(file):
    return redirect(f"/static/assets/webfonts/{file}")


if __name__ == "__main__":
    app.run(debug=True)
