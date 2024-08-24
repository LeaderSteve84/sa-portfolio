#!/usr/bin/env python3
"""home module"""
from flask import Blueprint, render_template
from app.models.featured_project import FeaturedProject

home_bp = Blueprint('home', __name__)


# home/landing page route
@home_bp.route("/", methods=['GET'], strict_slashes=False)
def home_page():
    """landing/home page route"""
    featured_projects = FeaturedProject.query.all()
    return render_template('home.html', featured_projects=featured_projects)
