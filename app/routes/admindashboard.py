#!/usr/bin/env python3
"""home module"""
from flask import Blueprint, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.contact import ContactMessage
from app.models.featured_project import FeaturedProject
from app.models.project_done import ProjectDone
from app.models.writing import Writing
from app.models.reference import Reference
from app.models import Admin

admindashboard_bp = Blueprint('admindashboard', __name__)


@admindashboard_bp.route("/admindashboard", methods=['GET'], strict_slashes=False)
@jwt_required()
def admindashboard_page():
    """Admin dashboard page route"""
    admin_id = get_jwt_identity() # Fetch and display data using the admin_id
    admin = Admin.query.filter_by(id=admin_id).first()
    if not admin:
        flash('You are not an admin', 'warning')
        return redirect(url_for('main.home.home_page'))
    contact_messages = ContactMessage.query.all()
    featured_projects = FeaturedProject.query.all()
    projects_done = ProjectDone.query.all()
    writings = Writing.query.all()
    references = Reference.query.all()

    return render_template(
        'admindashboard.html', contact_messages=contact_messages, references=references, featured_projects=featured_projects, projects_done=projects_done, writings=writings
    )
