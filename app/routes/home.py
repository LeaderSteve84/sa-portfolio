#!/usr/bin/env python3
"""home module"""
from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__)


# home/landing page route
@home_bp.route("/", methods=['GET'], strict_slashes=False)
@home_bp.route("/home", methods=['GET'], strict_slashes=False)
def home_page():
    """landing/home page route"""
    return render_template('home.html')
