#!/usr/bin/env python3
"""home module"""
from flask import Blueprint, render_template

about_bp = Blueprint('about', __name__)


# get the about me page
@about_bp.route("/about", methods=['GET'], strict_slashes=False)
def about_page():
    """about me route"""
    return render_template('about_me.html')
