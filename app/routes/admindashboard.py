#!/usr/bin/env python3
"""home module"""
from flask import Blueprint, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity

admindashboard_bp = Blueprint('admindashboard', __name__)


@admindashboard_bp.route("/admindashboard", methods=['GET'], strict_slashes=False)
@jwt_required()
def admindashboard_page():
    """Admin dashboard page route"""
    admin_id = get_jwt_identity() # Fetch and display data using the admin_id
    return render_template('admindashboard.html')
