from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Optional, URL


class ProjectDoneForm(FlaskForm):
    """Class to create form for adding projects Done"""
    title = StringField('Title', validators=[DataRequired()])
    project_type = StringField(
        'Type e.g personal, open source etc', validators=[DataRequired()]
    )
    description = TextAreaField(
        'Describe Project', validators=[DataRequired()]
    )
    stacks = StringField(
        'Stacks - Technologies Used', validators=[DataRequired()]
    )
    role = TextAreaField('Project Role', validators=[DataRequired()])
    date_cmptd = StringField('Completion Date', validators=[DataRequired()])
    video_link = StringField(
        'Video URL (Optional)',
        validators=[Optional(), URL(message='url not valid')]
    )
    submit = SubmitField('Add Project Done')
