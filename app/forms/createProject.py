from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, URL, Optional


class ProjectForm(FlaskForm):
    """Class to create form for projects done"""
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Describe Project', validators=[DataRequired()])
    image_link = StringField('Project Image URL', validators=[Optional()])  #, URL()])
    stacks = StringField('Stacks/Technologies Used', validators=[DataRequired()])
    domain_link = StringField('Project Domain URL', validators=[Optional()])  #, URL()])
    github_link = StringField('Project Github URL', validators=[Optional()])  #,, URL()])
    submit = SubmitField('Add Project Done')
