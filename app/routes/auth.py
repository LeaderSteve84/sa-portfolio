#!/usr/bin/env python3
"""home module"""
from flask import Blueprint, request, render_template, redirect, url_for, \
flash, request, jsonify, make_response
from flask_jwt_extended import create_access_token, set_access_cookies, unset_jwt_cookies
from app.forms.adminLogin import AdminLoginForm, AdminLogoutForm
from app.models import Admin
from werkzeug.security import check_password_hash
from datetime import timedelta

auth_bp = Blueprint('auth', __name__)


@auth_bp.route("/login", methods=['GET', 'POST'], strict_slashes=False)
def login():
    """route to login"""
    form = AdminLoginForm()
    if form.validate_on_submit():
        username_email = form.username_email.data
        password = form.password.data
        admin = Admin.query.filter((Admin.username == username_email) | (Admin.email == username_email)).first()
        if admin and check_password_hash(admin.password_hash, password):
            access_token = create_access_token(identity=admin.id, expires_delta=timedelta(hours=1))
            response = make_response(redirect(url_for('main.admindashboard.admindashboard_page')))
            set_access_cookies(response, access_token)
            return response
        else:
            flash('Invalid username/email or password', 'error')
            return render_template('adminlogin.html', form=form)
    return render_template('adminlogin.html', form=form)


@auth_bp.route("/logout-form", methods=['GET'], strict_slashes=False)
def logoutForm():
    """logout page"""
    form = AdminLogoutForm()
    return render_template('logout.html', form=form)


@auth_bp.route("/logout", methods=['POST'], strict_slashes=False)
def logout():
    """route to handle admin logout"""
    # if form.validate_on_submit:
    response = jsonify({"msg": "Logout successfully"})
    # unset the JWT cookies to log out
    unset_jwt_cookies(response)
    return redirect(url_for('main.home.home_page'))
