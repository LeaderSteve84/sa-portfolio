from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class AdminLoginForm(FlaskForm):
    username_email = StringField(label='Username/Email Address')
    password = PasswordField(label="Password")
    submit = SubmitField(label="Login")
