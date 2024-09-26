from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, URL, Optional


class TechWritingForm(FlaskForm):
    """Class to create form for technical writing"""
    title = StringField('Title', validators=[DataRequired()])
    image_link = StringField(
        'Image URL (Optional)', validators=[Optional(), URL()]
    )
    description = TextAreaField(
        'Technical Writing', validators=[DataRequired()]
    )
    published_link = StringField(
        'Published URL (Optional)', validators=[Optional(), URL()]
    )
    submit = SubmitField('Submit Technical Writing')
