from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, \
    URLField, SubmitField
from wtforms.validators import DataRequired, URL, Optional, Length


class ReferenceForm(FlaskForm):
    """Class to create form for creating reference"""
    reference_type = SelectField(
        'Select Type', choices=[
            ('testimony', 'Testimony'),
            ('quote', 'Quote'),
            ('feedback', 'Feedback')
        ], validators=[DataRequired()]
    )
    message = TextAreaField(
        'Message (minimum of 10 characters)',
        validators=[DataRequired(), Length(min=10)]
    )
    reference_link = URLField(
        'URL_Link (Optional)', validators=[Optional(), URL()]
    )
    contact = StringField(
        'Email | Mobile Contact (Optional)',
        validators=[Optional(), Length(max=100)]
    )
    name = StringField(
        'Name', validators=[DataRequired(), Length(max=100)]
    )
    designation = SelectField(
        'Select Your Designation',
        choices=[
            ('colleague', 'Colleague'),
            ('client', 'Client'),
            ('manager', 'Manager'),
            ('collaborator', 'Collaborator'),
            ('others', 'Others')
        ], validators=[DataRequired()]
    )
    submit = SubmitField('Submit Your Reference')
