#!/usr/bin/env python3
"""home module"""
from flask import Blueprint, render_template, flash, \
    url_for, current_app, redirect, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.forms.createWriting import TechWritingForm
from app.models import Writing, Admin

tech_writings_bp = Blueprint('tech_writings', __name__)
db = current_app.db
logger = current_app.logger


@tech_writings_bp.route(
    "/writings/new",
    methods=['GET', 'POST'],
    strict_slashes=False
)
def create_writing():
    """create writing done"""
    form = TechWritingForm()
    if form.validate_on_submit():
        new_writing = Writing(
            title=form.title.data,
            image_link=form.image_link.data,
            description=form.description.data,
            published_link=form.published_link.data
        )
        try:
            db.session.add(new_writing)
            db.session.commit()
            flash('Tech writing added successfully', 'success')
            return redirect(url_for('main.tech_writings.list_writings'))
        except Exception as e:
            db.session.rollback()
            flash("Error: " + str(e), "danger")
            return redirect(url_for('main.tech_writings.create_writings'))
    else:
        if form.errors != {}:
            for error_message in form.errors.values():
                flash(
                    f"Error creating your technical writting: \
                        {error_message}",
                    "error"
                )
    return render_template('create_writing.html', form=form)


@tech_writings_bp.route("/writings", methods=['GET'], strict_slashes=False)
@jwt_required()
def list_writings():
    """get list of all technical writings"""
    admin_id = get_jwt_identity()
    admin = Admin.query.filter_by(id=admin_id).first()
    if not admin:
        flash('You are not an admin', 'warning')
        return redirect(url_for('main.home.home_page'))
    writings = Writing.query.all()
    return render_template('list_writings.html', writings=writings)


@tech_writings_bp.route(
    "/writings/view", methods=['GET'], strict_slashes=False
)
def view_writings():
    """get list of all technical writings"""
    writings = Writing.query.all()
    return render_template('view_writings.html', writings=writings)


@tech_writings_bp.route(
    "/writings/<string:writing_id>/edit",
    methods=['GET'],
    strict_slashes=False
)
@jwt_required()
def edit_writing(writing_id):
    """edit a created technical writings"""
    admin_id = get_jwt_identity()
    admin = Admin.query.filter_by(id=admin_id).first()
    if not admin:
        flash('You are not an admin', 'warning')
        return redirect(url_for('main.home.home_page'))
    writing = Writing.query.get_or_404(writing_id)
    return render_template('edit_writing.html', writing=writing)


@tech_writings_bp.route(
    "/writings/<string:writing_id>/update",
    methods=['POST'],
    strict_slashes=False
)
def update_writing(writing_id):
    """update a technical writing"""
    writing = Writing.query.get_or_404(writing_id)

    writing.title = request.form['title']
    writing.image_link = request.form.get('image_link', writing.image_link)
    writing.description = request.form['description']
    writing.published_link = request.form.get(
        'published_link',
        writing.published_link
    )
    try:
        db.session.commit()
        flash('Technical writing updated successfully', 'success')
        return redirect(url_for("main.tech_writings.list_writings"))
    except Exception as e:
        db.session.rollback()
        flash("Error: " + str(e), "danger")
        return redirect(url_for("main.tech_writings.list_writings"))


@tech_writings_bp.route(
    "/writings/<string:writing_id>/delete",
    methods=['POST'],
    strict_slashes=False
)
def delete_writing(writing_id):
    """delete a Technical writing"""
    writing = Writing.query.get_or_404(writing_id)
    if writing:
        try:
            db.session.delete(writing)
            db.session.commit()
            flash('Technical writing deleted successfully!', 'success')
            return redirect(url_for('main.tech_writings.list_writings'))
        except Exception as e:
            db.session.rollback()
            flash("Error: " + str(e), "danger")
            return redirect(url_for('main.tech_writings.list_writings'))
    else:
        flash('Technical Writing not found', 'error')
    return redirect(url_for('main.tech_writings.list_writings'))
