#!/usr/bin/env python3
"""module for portfolio route"""
from flask import Blueprint, render_template

portfolio_bp = Blueprint('portfolio', __name__)


@portfolio_bp.route("/portfolio", methods=['GET'], strict_slashes=False)
def portfolio_page():
    """portfolio route"""
    return render_template('portfolio.html')
