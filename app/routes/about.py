#!/usr/bin/env python3
"""home module"""
from flask import Blueprint, render_template, current_app

about_bp = Blueprint('about', __name__)
cache = current_app.cache


# get the about me page
@about_bp.route("/about", methods=['GET'], strict_slashes=False)
@cache.cached(timeout=3600)
def about_page():
    """about me route"""
    return render_template('about_me.html')
