from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = '1234567890'


ADMIN_EMAIL = "admin@email.com"
ADMIN_PASSWORD = "12345678"


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[
                        DataRequired(message="Please add an Email"), Email(message="This email is not valid")])
    password = PasswordField(label='Password', validators=[
                             DataRequired(message="Please add a Password"), Length(min=8, message="You must type at least 8 characters")])
    submit = SubmitField("Login")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        user_email = form.email.data
        user_password = form.password.data
        if user_email == ADMIN_EMAIL and user_password == ADMIN_PASSWORD:
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
