from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Optional


class ContactForm(FlaskForm):
    """Class to create form for creating contact messages"""
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    email = StringField(
        'Email', validators=[DataRequired(), Length(max=1000), Email()]
    )
    subject = StringField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    status = StringField('Status', validators=[Optional()])
    submit = SubmitField('Send Message')
