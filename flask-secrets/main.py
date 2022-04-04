from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[
        DataRequired(message="This field is required"), 
        Email(message="Provide a valid email address")])
    password = PasswordField(label='Password', validators=[
        DataRequired(message="This field is required"), 
        Length(min = 8, message="Password must contain at least 8 characters")])
    submit = SubmitField(label="Log In")

app = Flask(__name__)

app.secret_key = "smkhjgr77632."

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        entered_user = login_form.email.data
        entered_password = login_form.password.data
        if entered_password == "12345678" and entered_user == "admin@email.com":
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)