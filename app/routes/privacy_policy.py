#!/usr/bin/env python3
"""private policy module"""
from flask import Blueprint, render_template, current_app

privacy_policy_bp = Blueprint('privacy_policy', __name__)
cache = current_app.cache


@privacy_policy_bp.route(
    "/privacy-policy", methods=['GET'], strict_slashes=False
)
@cache.cached(timeout=3600)
def privacy_policy_page():
    """privacy policy page route"""
    return render_template('privacy_policy.html')
