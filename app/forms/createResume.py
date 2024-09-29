from flask_wtf import FlaskForm
from wtforms import URLField, SubmitField
from wtforms.validators import DataRequired, URL, Optional


class ResumeForm(FlaskForm):
    """Class to create form for creating resume"""
    resume_image1_link = URLField(
        'Resume Image 1 Link',
        validators=[DataRequired(), URL(message='url not valid')]
    )
    resume_image2_link = URLField(
        'Resume Image 2 Link (Optional)',
        validators=[Optional(), URL(message='url not valid')]
    )
    resume_image3_link = URLField(
        'Resume Image 3 Link (Optional)',
        validators=[Optional(), URL(message='url not valid')]
    )
    resume_image4_link = URLField(
        'Resume Image 4 Link (Optional)',
        validators=[Optional(), URL(message='url not valid')]
    )
    resume_download_link = URLField(
        'Resume Download Link (Optional)',
        validators=[Optional(), URL(message='url not valid')]
    )
    submit = SubmitField('Submit Your Resume')
