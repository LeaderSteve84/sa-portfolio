#!/usr/bin/env python3
"""home module"""
from flask import Blueprint, render_template, flash, url_for, current_app, redirect, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.forms.createProject import ProjectForm
from app.models.project import Project
from flask_wtf.csrf import generate_csrf

projects_bp = Blueprint('projects', __name__)
db = current_app.db
logger = current_app.logger

@projects_bp.route("/projects/new", methods=['GET', 'POST'], strict_slashes=False)
# @jwt_required()
def create_project():
    """create projects done"""
    # admin_id = get_jwt_identity()
    token = generate_csrf()
    print(f"generated csrf token: {token}")
    form = ProjectForm()
    if form.validate_on_submit():
        new_project = Project(
            title = form.title.data,
            description = form.description.data,
            image_link = form.image_link.data,
            stacks = form.stacks.data,
            domain_link = form.domain_link.data,
            github_link = form.github_link.data
        )
        logger.info(new_project.image_link, new_project.domain_link)
        db.session.add(new_project)
        db.session.commit()
        flash('Project done added successfully', 'success')
        return redirect(url_for('main.projects.list_projects'))
    return render_template('create_project.html', form=form)


@projects_bp.route("/projects", methods=['GET'], strict_slashes=False)
def list_projects():
        """get list of all projects done"""
        projects = Project.query.all()
        return render_template('list_projects.html', projects=projects)


@projects_bp.route("/projects/view", methods=['GET'], strict_slashes=False)
def view_projects():
        """get list of all projects done"""
        projects = Project.query.all()
        return render_template('all_projects.html', projects=projects)

@projects_bp.route("/projects/<int:project_id>/edit", methods=['GET'], strict_slashes=False)
def edit_project(project_id):
        """edit a created projects done"""
        project = Project.query.get_or_404(project_id)
        return render_template('edit_project.html', project=project)


@projects_bp.route("/projects/<int:project_id>/update", methods=['POST'], strict_slashes=False)
def update_project(project_id):
    """update a projects done"""
    project = Project.query.get_or_404(project_id)
    
    project.title = request.form['title']
    project.description = request.form['description']
    project.image_link = request.form.get('image_link', project.image_link)
    project.stacks = request.form['stacks']
    project.domain_link = request.form.get('domain_link', project.domain_link)
    project.github_link = request.form.get('github_link', project.github_link)

    db.session.commit()
    flash('Project updated successfully', 'success')

    return redirect(url_for("main.projects.list_projects"))


@projects_bp.route("/projects/<int:project_id>/delete", methods=['POST'], strict_slashes=False)
def delete_project(project_id):
    """delete a projects done"""
    project = Project.query.get_or_404(project_id)
    if project:
        db.session.delete(project)
        db.session.commit()
        flash('Project deleted successfully!', 'success')
    else:
        flash('Project not found', 'error')
    return redirect(url_for('main.projects.list_projects'))
