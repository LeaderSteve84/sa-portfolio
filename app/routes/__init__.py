#!/usr/bin/env python3
"""routes package init"""
from flask import Blueprint
from . import home
from . import projects
from . import tech_writings
from . import auth
from . import about
from . import admindashboard

bp = Blueprint('main', __name__)

# register blueprint into main "bp"
bp.register_blueprint(home.home_bp)
bp.register_blueprint(projects.projects_bp)
bp.register_blueprint(tech_writings.tech_writings_bp)
bp.register_blueprint(auth.auth_bp)
bp.register_blueprint(about.about_bp)
bp.register_blueprint(admindashboard.admindashboard_bp)
