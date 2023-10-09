from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def wrapper():
        function_var = func()
        return f"<b>" + function_var + "<b/>"
    return wrapper


def make_emphasis(func):
    def wrapper():
        function_var = func()
        return f"<em>" + function_var + "<em/>"
    return wrapper


def make_underlined(func):
    def wrapper():
        function_var = func()
        return f"<u>" + function_var + "<u/>"
    return wrapper


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def fuck():
    return "bold faggot..."


if __name__ == '__main__':
    app.run(debug=True)
