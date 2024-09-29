from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, URL, Optional


class FeaturedProjectForm(FlaskForm):
    """Class to create form for adding featured projects"""
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    image_link = StringField(
        'Image URL (Optional)',
        validators=[Optional(), URL(message='url not valid')]
    )
    stacks = StringField(
        'Stacks - Technologies Used',
        validators=[DataRequired()]
    )
    role = TextAreaField('Your Role', validators=[DataRequired()])
    challenges = TextAreaField(
        'Challenges Overcome', validators=[DataRequired()]
    )
    date_cmptd = StringField(
        'Completion Date', validators=[DataRequired()]
    )
    domain_link = StringField(
        'Domain URL (Optional)',
        validators=[Optional(), URL(message='url not valid')]
    )
    github_link = StringField(
        'Github URL (Optional)',
        validators=[Optional(), URL(message='url not valid')]
    )
    video_link = StringField(
        'Video URL (Optional)',
        validators=[Optional(), URL(message='url not valid')]
    )
    submit = SubmitField('Add Featured Project')
