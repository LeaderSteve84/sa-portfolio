from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, URL, Optional


class TechWritingForm(FlaskForm):
    """Class to create form for technical writing"""
    title = StringField('Title', validators=[DataRequired()])
    image_link = StringField('Technical Writing Image URL', validators=[Optional()])  #, URL()])
    description = TextAreaField('Describe Project', validators=[DataRequired()])
    published_link = StringField('Technical Writing Published URL', validators=[Optional()])  #, URL()])
    submit = SubmitField('Add Technical Writing')
