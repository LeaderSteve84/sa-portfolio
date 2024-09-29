#!/usr/bin/env python3
"""home module"""
from flask import Blueprint, render_template, flash, \
    url_for, current_app, redirect, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.forms.createResume import ResumeForm
from app.models import Resume, Admin

resume_bp = Blueprint('resume', __name__)
db = current_app.db
cache = current_app.cache
logger = current_app.logger


@resume_bp.route(
    "/resume/new", methods=['GET', 'POST'], strict_slashes=False
)
def create_resume():
    """create resume"""
    form = ResumeForm()
    if form.validate_on_submit():
        resume = Resume(
            resume_image1_link=form.resume_image1_link.data,
            resume_image2_link=form.resume_image2_link.data,
            resume_image3_link=form.resume_image3_link.data,
            resume_image4_link=form.resume_image4_link.data,
            resume_download_link=form.resume_download_link.data
        )
        try:
            db.session.add(resume)
            db.session.commit()
            flash('Resume added successfully', 'success')
            return redirect(url_for('main.resume.list_resume'))
        except Exception as e:
            db.session.rollback()
            flash("Error: " + str(e), "danger")
            return redirect(url_for('main.resume.create_resume'))
    else:
        if form.errors != {}:
            for error_message in form.errors.values():
                flash(
                    f"Error creating your resume: {error_message}",
                    "error"
                )
    return render_template('create_resume.html', form=form)


@resume_bp.route("/resume", methods=['GET'], strict_slashes=False)
@jwt_required()
def list_resume():
    """list the resume"""
    admin_id = get_jwt_identity()
    admin = Admin.query.filter_by(id=admin_id).first()
    if not admin:
        flash('You are not an admin', 'warning')
        return redirect(url_for('main.home.home_page'))
    resume = Resume.query.all()
    return render_template('list_resume.html', resume=resume)


@resume_bp.route("/resume/view", methods=['GET'], strict_slashes=False)
@cache.cached(timeout=3600)
def view_resume():
    """view resume"""
    resume = Resume.query.all()
    return render_template('view_resume.html', resume=resume)


@resume_bp.route(
    "/resume/<string:resume_id>/edit",
    methods=['GET', 'POST'],
    strict_slashes=False
)
def edit_resume(resume_id):
    """edit and update a created resume"""
    resume = Resume.query.get_or_404(resume_id)
    form = ResumeForm(obj=resume)
    if form.validate_on_submit():
        resume.resume_image1_link = form.resume_image1_link.data
        resume.resume_image2_link = form.resume_image2_link.data
        resume.resume_image3_link = form.resume_image3_link.data
        resume.resume_image4_link = form.resume_image4_link.data
        resume.resume_download_link = form.resume_download_link.data
        try:
            db.session.commit()
            flash('Resume updated successfully', 'success')
            return redirect(url_for('main.resume.list_resume'))
        except Exception as e:
            db.session.rollback()
            flash("Error: " + str(e), "danger")
            return redirect(url_for('main.resume.list_resume'))
    else:
        if form.errors != {}:
            for error_message in form.errors.values():
                flash(f"Error updating your resume: {error_message}", "error")
    return render_template('edit_resume.html', form=form, resume=resume)


@resume_bp.route(
    "/resume/<string:resume_id>/delete",
    methods=['POST'],
    strict_slashes=False
)
def delete_resume(resume_id):
    """delete a resume"""
    resume = Resume.query.get_or_404(resume_id)
    if resume:
        try:
            db.session.delete(resume)
            db.session.commit()
            flash('Resume deleted successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash("Error: " + str(e), "danger")
            return redirect(url_for('main.resume.list_resume'))
    else:
        flash('Resume not found', 'error')
    return redirect(url_for('main.resume.list_resume'))
