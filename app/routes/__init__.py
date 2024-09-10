#!/usr/bin/env python3
"""routes package init"""
from flask import Blueprint
from . import home
from . import featured_projects
from . import projects_done
from . import tech_writings
from . import auth
from . import about
from . import admindashboard
from . import references
from . import resume
from . import contacts
from . import privacy_policy
from . import disclaimer_or_terms

bp = Blueprint('main', __name__)

# register blueprint into main "bp"
bp.register_blueprint(home.home_bp)
bp.register_blueprint(featured_projects.featured_projects_bp)
bp.register_blueprint(projects_done.projects_done_bp)
bp.register_blueprint(tech_writings.tech_writings_bp)
bp.register_blueprint(auth.auth_bp)
bp.register_blueprint(about.about_bp)
bp.register_blueprint(admindashboard.admindashboard_bp)
bp.register_blueprint(references.references_bp)
bp.register_blueprint(resume.resume_bp)
bp.register_blueprint(contacts.contacts_bp)
bp.register_blueprint(privacy_policy.privacy_policy_bp)
bp.register_blueprint(disclaimer_or_terms.disclaimer_or_terms_bp)
