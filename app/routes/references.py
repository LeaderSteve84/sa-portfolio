#!/usr/bin/env python3
"""home module"""
from flask import Blueprint, render_template, flash, url_for, current_app, redirect, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.forms.createReference import ReferenceForm
from app.models.reference import Reference
from flask_wtf.csrf import generate_csrf

references_bp = Blueprint('references', __name__)
db = current_app.db
logger = current_app.logger

@references_bp.route("/reference/new", methods=['GET', 'POST'], strict_slashes=False)
# @jwt_required()
def create_reference():
    """create reference"""
    # admin_id = get_jwt_identity()
    token = generate_csrf()
    print(f"generated csrf token: {token}")
    form = ReferenceForm()
    if form.validate_on_submit():
        reference = Reference(
            reference_type = form.reference_type.data,
            message = form.message.data,
            reference_link = form.reference_link.data,
            contact = form.contact.data,
            name = form.name.data,
            designation = form.designation.data
        )
        db.session.add(reference)
        db.session.commit()
        flash('Reference added successfully', 'success')
        return redirect(url_for('main.references.view_references'))
    return render_template('create_reference.html', form=form)


@references_bp.route("/references", methods=['GET'], strict_slashes=False)
def list_references():
        """get list of all references"""
        references = Reference.query.all()
        return render_template('list_references.html', references=references)


@references_bp.route("/references/view", methods=['GET'], strict_slashes=False)
def view_references():
        """get list of all reference"""
        references = Reference.query.all()
        return render_template('view_references.html', references=references)

@references_bp.route("/reference/<int:reference_id>/edit", methods=['GET', 'POST'], strict_slashes=False)
def edit_reference(reference_id):
        """edit and update a created reference"""
        reference = Reference.query.get_or_404(reference_id)
        form = ReferenceForm(obj=reference)
        if form.validate_on_submit():
            reference.reference_type = form.reference_type.data
            reference.message = form.message.data
            reference.reference_link = form.reference_link.data
            reference.contact = form.contact.data
            reference.name = form.name.data
            reference.designation = form.designation.data
            db.session.commit()
            flash('Reference updated successfully', 'success')
            return redirect(url_for('main.references.list_references'))
        return render_template('edit_reference.html', form=form, reference=reference)


@references_bp.route("/reference/<int:reference_id>/delete", methods=['POST'], strict_slashes=False)
def delete_reference(reference_id):
    """delete a reference"""
    reference = Reference.query.get_or_404(reference_id)
    if reference:
        db.session.delete(reference)
        db.session.commit()
        flash('Reference deleted successfully!', 'success')
    else:
        flash('Reference not found', 'error')
    return redirect(url_for('main.references.list_references'))
