#!/usr/bin/env python3
"""private policy module"""
from flask import Blueprint, render_template

privacy_policy_bp = Blueprint('privacy_policy', __name__)


@privacy_policy_bp.route(
    "/privacy-policy", methods=['GET'], strict_slashes=False
)
def privacy_policy_page():
    """privacy policy page route"""
    return render_template('privacy_policy.html')
