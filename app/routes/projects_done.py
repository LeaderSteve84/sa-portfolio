#!/usr/bin/env python3
"""module for project done routes"""
from flask import Blueprint, render_template, flash, url_for, current_app, redirect, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.forms.createProjectDone import ProjectDoneForm
from app.models.project_done import ProjectDone
from flask_wtf.csrf import generate_csrf

projects_done_bp = Blueprint('projects_done', __name__)
db = current_app.db
logger = current_app.logger

@projects_done_bp.route("/project_done/new", methods=['GET', 'POST'], strict_slashes=False)
# @jwt_required()
def create_project_done():
    """create projects done"""
    # admin_id = get_jwt_identity()
    token = generate_csrf()
    print(f"generated csrf token: {token}")
    form = ProjectDoneForm()
    if form.validate_on_submit():
        new_project = ProjectDone(
            title = form.title.data,
            project_type = form.project_type.data,
            description = form.description.data,
            stacks = form.stacks.data,
            role = form.role.data,
            date_cmptd = form.date_cmptd.data,
            video_link = form.video_link.data
        )
        db.session.add(new_project)
        db.session.commit()
        flash('Project done added successfully', 'success')
        return redirect(url_for('main.projects_done.list_projects_done'))
    return render_template('create_project_done.html', form=form)


@projects_done_bp.route("/project_done", methods=['GET'], strict_slashes=False)
def list_projects_done():
        """get list of all projects done"""
        projects_done = ProjectDone.query.all()
        return render_template('list_projects_done.html', projects_done=projects_done)


@projects_done_bp.route("/project_done/view", methods=['GET'], strict_slashes=False)
def view_projects_done():
        """get list of all projects done"""
        projects_done = ProjectDone.query.all()
        return render_template('view_projects_done.html', projects_done=projects_done)

@projects_done_bp.route("/projects_done/<int:project_done_id>/edit", methods=['GET'], strict_slashes=False)
def edit_project_done(project_done_id):
        """edit a created project done"""
        project_done = ProjectDone.query.get_or_404(project_done_id)
        return render_template('edit_project_done.html', project_done=project_done)


@projects_done_bp.route("/project_done/<int:project_done_id>/update", methods=['POST'], strict_slashes=False)
def update_project_done(project_done_id):
    """update a projects done"""
    project_done = ProjectDone.query.get_or_404(project_done_id)
    
    project_done.title = request.form['title']
    project_done.project_type = request.form.get('project_type', project_done.project_type)
    project_done.description = request.form['description']
    project_done.stacks = request.form['stacks']
    project_done.role = request.form['role']
    project_done.date_cmptd = request.form['date_cmptd']
    project_done.video_link = request.form.get('video_link', project_done.video_link)

    db.session.commit()
    flash('Project Done updated successfully', 'success')

    return redirect(url_for("main.projects_done.list_projects_done"))


@projects_done_bp.route("/project_done/<int:project_done_id>/delete", methods=['POST'], strict_slashes=False)
def delete_project_done(project_done_id):
    """delete a Project Done"""
    project_done = ProjectDone.query.get_or_404(project_done_id)
    if project_done:
        db.session.delete(project_done)
        db.session.commit()
        flash('Project done deleted successfully!', 'success')
    else:
        flash('Project done not found', 'error')
    return redirect(url_for('main.projects_done.list_projects_done'))
