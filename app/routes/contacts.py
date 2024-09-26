#!/usr/bin/env python3
"""home module"""
from flask import Blueprint, render_template, flash, url_for, \
    current_app, redirect, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.admin import Admin
from app.forms.createMessage import ContactForm
from app.models.contact import ContactMessage

contacts_bp = Blueprint('contacts', __name__)
db = current_app.db
logger = current_app.logger


@contacts_bp.route("/contacts", methods=['GET', 'POST'], strict_slashes=False)
def create_contact_message():
    """create contact message"""
    form = ContactForm()
    if form.validate_on_submit():
        contact_message = ContactMessage(
            name=form.name.data,
            email=form.email.data,
            subject=form.subject.data,
            message=form.message.data
        )
        db.session.add(contact_message)
        db.session.commit()
        flash(
            "Your message has been successfully submitted. \
                We'll get back to you soon. Thank You!",
            'success'
        )
        return redirect(url_for('main.contacts.create_contact_message'))
    else:
        if form.errors != {}:
            for error_message in form.errors.values():
                flash(
                    'There is an error creating your contact message', 'error'
                )
    return render_template('create_contact_message.html', form=form)


@contacts_bp.route("/contacts/view", methods=['GET'], strict_slashes=False)
@jwt_required()
def view_contact_messages():
    """view all contacts"""
    admin_id = get_jwt_identity()
    admin = Admin.query.filter_by(id=admin_id).first()
    if not admin:
        flash('You are not an admin', 'warning')
        return redirect(url_for('main.home.home_page'))
    contact_messages = ContactMessage.query.all()
    return render_template(
        'view_contact_messages.html', contact_messages=contact_messages
    )


@contacts_bp.route(
    "/contact/<string:message_id>/edit",
    methods=['GET', 'POST'],
    strict_slashes=False
)
def update_contact_message(message_id):
    '''edit and update a created reference'''
    contact_message = ContactMessage.query.get_or_404(message_id)
    form = ContactForm(obj=contact_message)
    if form.validate_on_submit():
        contact_message.name = form.name.data
        contact_message.email = form.email.data
        contact_message.subject = form.subject.data
        contact_message.message = form.message.data
        contact_message.status = form.status.data
        db.session.commit()
        flash('Contact Message updated successfully', 'success')
        return redirect(url_for('main.contacts.view_contact_messages'))
    else:
        if form.errors != {}:
            for error_message in form.errors.values():
                flash(
                    'There is an error updating your \
                        contact message: {error_message}',
                    'error'
                )
    return render_template(
        'update_contact_message.html',
        form=form,
        contact_message=contact_message
    )


@contacts_bp.route(
    "/contact/<string:message_id>/delete",
    methods=['POST'], strict_slashes=False
)
def delete_contact_message(message_id):
    """delete a contact"""
    contact_message = ContactMessage.query.get_or_404(message_id)
    if contact_message:
        db.session.delete(contact_message)
        db.session.commit()
        flash('Contact message deleted successfully!', 'success')
    else:
        flash('Contact message not found', 'error')
    return redirect(url_for('main.contacts.view_contact_messages'))
