#!/usr/bin/env python3
"""disclaimer or terms module"""
from flask import Blueprint, render_template, current_app

disclaimer_or_terms_bp = Blueprint('disclaimer_or_terms', __name__)
cache = current_app.cache


@disclaimer_or_terms_bp.route(
    "/disclaimer-or-terms",
    methods=['GET'],
    strict_slashes=False
)
@cache.cached(timeout=3600)
def disclaimer_or_terms_page():
    """disclaimer or terms page route"""
    return render_template('disclaimer_or_terms.html')
