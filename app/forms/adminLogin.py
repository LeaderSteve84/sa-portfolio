from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class AdminLoginForm(FlaskForm):
    username_email = StringField('Username/Email Address', validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class AdminLogoutForm(FlaskForm):
    submit = SubmitField("Logout")
