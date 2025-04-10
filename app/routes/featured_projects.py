#!/usr/bin/env python3
"""home module"""
from flask import Blueprint, render_template, flash, url_for, \
    current_app, redirect, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.forms.createFeaturedProject import FeaturedProjectForm
from app.models import FeaturedProject, Admin

featured_projects_bp = Blueprint('featured_projects', __name__)
db = current_app.db
cache = current_app.cache
logger = current_app.logger


@featured_projects_bp.route(
    "/featured_projects/new",
    methods=['GET', 'POST'],
    strict_slashes=False
)
def create_featured_project():
    """create featured projects done"""
    form = FeaturedProjectForm()
    if form.validate_on_submit():
        new_project = FeaturedProject(
            title=form.title.data,
            description=form.description.data,
            image_link=form.image_link.data,
            stacks=form.stacks.data,
            role=form.role.data,
            challenges=form.challenges.data,
            date_cmptd=form.date_cmptd.data,
            domain_link=form.domain_link.data,
            github_link=form.github_link.data,
            video_link=form.video_link.data
        )
        try:
            db.session.add(new_project)
            db.session.commit()
            flash('Featured project added successfully', 'success')
            return redirect(
                url_for('main.featured_projects.list_featured_projects')
            )
        except Exception as e:
            db.session.rollback()
            flash("Error: " + str(e), "danger")
            return redirect(
                url_for('main.featured_projects.create_featured_project')
            )
    else:
        if form.errors != {}:
            for error_message in form.errors.values():
                flash(
                    f"Error creating featured project: {error_message}",
                    "error"
                )
        return render_template('create_featured_project.html', form=form)


@featured_projects_bp.route(
    "/featured_projects", methods=['GET'], strict_slashes=False
)
@jwt_required()
def list_featured_projects():
    """get list of all featured projects"""
    admin_id = get_jwt_identity()
    admin = Admin.query.filter_by(id=admin_id).first()
    if not admin:
        flash('You are not an admin', 'warning')
        return redirect(url_for('main.home.home_page'))
    featured_projects = FeaturedProject.query.all()
    return render_template(
        'list_featured_projects.html',
        featured_projects=featured_projects
    )


@featured_projects_bp.route(
    "/featured_projects/view", methods=['GET'], strict_slashes=False
)
@cache.cached(timeout=3600)
def view_featured_projects():
    """get list of all featured projects"""
    featured_projects = FeaturedProject.query.all()
    return render_template(
        'view_featured_projects.html',
        featured_projects=featured_projects
    )


@featured_projects_bp.route(
    "/featured_projects/<string:featured_project_id>/edit",
    methods=['GET'], strict_slashes=False
)
@jwt_required()
def edit_featured_project(featured_project_id):
    """edit a created featured projects"""
    admin_id = get_jwt_identity()
    admin = Admin.query.filter_by(id=admin_id).first()
    if not admin:
        flash('You are not an admin', 'warning')
        return redirect(url_for('main.home.home_page'))
    featured_project = FeaturedProject.query.get_or_404(featured_project_id)
    return render_template(
        'edit_featured_project.html',
        featured_project=featured_project
    )


@featured_projects_bp.route(
    "/featured_projects/<string:featured_project_id>/update",
    methods=['POST'],
    strict_slashes=False
)
def update_featured_project(featured_project_id):
    """update a featured projects"""
    featured_project = FeaturedProject.query.get_or_404(featured_project_id)

    featured_project.title = request.form['title']
    featured_project.description = request.form['description']
    featured_project.image_link = request.form.get(
        'image_link', featured_project.image_link
    )
    featured_project.stacks = request.form['stacks']
    featured_project.role = request.form['role']
    featured_project.challenges = request.form['challenges']
    featured_project.date_cmptd = request.form['date_cmptd']
    featured_project.domain_link = request.form.get(
        'domain_link', featured_project.domain_link
    )
    featured_project.github_link = request.form.get(
        'github_link', featured_project.github_link
    )
    featured_project.video_link = request.form.get(
        'video_link', featured_project.video_link
    )
    try:
        db.session.commit()
        flash('Featured project updated successfully', 'success')
        return redirect(
            url_for(
                "main.featured_projects.list_featured_projects"
            )
        )
    except Exception as e:
        db.session.rollback()
        flash("Error: " + str(e), "danger")
        return redirect(
            url_for("main.featured_projects.list_featured_projects")
        )


@featured_projects_bp.route(
    "/featured_projects/<string:featured_project_id>/delete",
    methods=['POST'], strict_slashes=False
)
def delete_featured_project(featured_project_id):
    """delete a featured projects"""
    featured_project = FeaturedProject.query.get_or_404(featured_project_id)
    if featured_project:
        try:
            db.session.delete(featured_project)
            db.session.commit()
            flash('Featured project deleted successfully!', 'success')
            return redirect(
                url_for('main.featured_projects.list_featured_projects')
            )
        except Exception as e:
            db.session.rollback()
            flash("Error: " + str(e), "danger")
            return redirect(
                url_for('main.featured_projects.list_featured_projects')
            )
    else:
        flash('Featured project not found', 'error')
        return redirect(
            url_for('main.featured_projects.list_featured_projects')
        )
