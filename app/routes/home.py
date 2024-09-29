#!/usr/bin/env python3
"""home module"""
from flask import Blueprint, render_template, current_app
from app.models.featured_project import FeaturedProject

home_bp = Blueprint('home', __name__)
cache = current_app.cache


# home/landing page route
@home_bp.route("/", methods=['GET'], strict_slashes=False)
@cache.cached(timeout=3600)
def home_page():
    """landing/home page route"""
    featured_projects = FeaturedProject.query.all()
    return render_template('home.html', featured_projects=featured_projects)
