#!/usr/bin/env python3
"""home module"""
from flask import Blueprint, render_template
tech_writings_bp = Blueprint('tech_writings', __name__)

# create technical writings
@tech_writings_bp.route("/tech_writings", methods=['POST'], strict_slashes=False)
def create_technical_writings():
    """routes for technical writings"""
    return 'Create Technical writing endpoint'


# get list of technical writings
@tech_writings_bp.route("/tech_writings", methods=['GET'], strict_slashes=False)
def get_technical_writings():
    """routes for technical writings"""
    return render_template('tech-writings.html')


# update a technical writings
@tech_writings_bp.route("/tech_writings/update/<id>", methods=['PUT'], strict_slashes=False)
def update_technical_writings(id):
    """routes for technical writings"""
    return f'Update Technical writing endpoint {id}'


# delete technical writings
@tech_writings_bp.route("/tech_writings/delete/<id>", methods=['DELETE'], strict_slashes=False)
def delete_technical_writings(id):
    """routes for technical writings"""
    return f'Delete Technical writing endpoint {id}'
