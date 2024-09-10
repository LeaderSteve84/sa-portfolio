from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, URL, Optional


class FeaturedProjectForm(FlaskForm):
    """Class to create form for adding featured projects"""
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    image_link = StringField('Image URL (Optional)', validators=[Optional()])  #, URL()])
    stacks = StringField('Stacks - Technologies Used', validators=[DataRequired()])
    role = TextAreaField('Your Role', validators=[DataRequired()])
    challenges = TextAreaField('Challenges Overcome', validators=[DataRequired()])
    date_cmptd = StringField('Completion Date', validators=[DataRequired()])
    domain_link = StringField('Domain URL (Optional)', validators=[Optional()])  #, URL()])
    github_link = StringField('Github URL (Optional)', validators=[Optional()])  #,, URL()])
    video_link = StringField('Video URL (Optional)', validators=[Optional()])
    submit = SubmitField('Add Featured Project')
