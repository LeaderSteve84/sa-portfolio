#!/usr/bin/env python3
"""home module"""
from flask import Blueprint, render_template

admindashboard_bp = Blueprint('admindashboard', __name__)


# admin dashboard route
@admindashboard_bp.route("/admindashboard", methods=['GET'], strict_slashes=False)
def admindashboard_page():
    """Admin dashboard page route"""
    return render_template('admindashboard.html')
