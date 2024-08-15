#!/usr/bin/env python3
"""home module"""
from flask import Blueprint, render_template
projects_bp = Blueprint('projects', __name__)

# create projects done
@projects_bp.route("/projects", methods=['POST'], strict_slashes=False)
def create_projects():
    """get all projects done"""
    return "Project post endpoint"


# get list of all projects done
@projects_bp.route("/projects", methods=['GET'], strict_slashes=False)
def get_projects():
        """get all projects done"""
        return render_template('projects.html')


# update a project done
@projects_bp.route("/projects/update/<id>") #, methods=['PUT'], strict_slashes=False)
def update_projects(id):
    """get all projects done"""
    return f"This is update {id}"


# delete a project done
@projects_bp.route("/projects/delete/<id>", methods=['POST'], strict_slashes=False)
def delete_projects(id):
    """get all projects done"""
    return f"Project delete endpoint {id}"
