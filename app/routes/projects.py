#!/usr/bin/env python3
"""home module"""
from flask import Blueprint, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity
projects_bp = Blueprint('projects', __name__)

@projects_bp.route("/projects", methods=['POST'], strict_slashes=False)
@jwt_required()
def create_projects():
    """create projects done"""
    admin_id = get_jwt_identity()
    return "Project post endpoint"


# get list of all projects done
@projects_bp.route("/projects", methods=['GET'], strict_slashes=False)
def get_projects():
        """get all projects done"""
        return render_template('projects.html')


@projects_bp.route("/projects/update/<id>") #, methods=['PUT'], strict_slashes=False)
def update_projects(id):
    """update a projects done"""
    return f"This is update {id}"


@projects_bp.route("/projects/delete/<id>", methods=['POST'], strict_slashes=False)
def delete_projects(id):
    """delete a projects done"""
    return f"Project delete endpoint {id}"
