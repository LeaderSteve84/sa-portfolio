#!/usr/bin/env python3
"""home module"""
from flask import Blueprint, request, render_template, redirect, url_for
from app.forms.adminLogin import AdminLoginForm

auth_bp = Blueprint('auth', __name__)


@auth_bp.route("/loginForm", methods=['GET', 'POST'], strict_slashes=False)
def admin_login_form():
    """route to admin login form"""
    form = AdminLoginForm()
    return render_template('adminlogin.html', form=form)


@auth_bp.route("/login", methods=['GET', 'POST'], strict_slashes=False)
def login():
    """route to login"""
    # form = AdminLoginForm()
    if request.method == 'POST':
        username = request.form['username_email']
        password = request.form['password']
        if username and password:
            print(f"Admin {username}, {password}")
            return redirect(url_for('main.admindashboard.admindashboard_page'))
        else:
            error = "credential incomplete"
            form = AdminLoginForm()
            return render_template('adminlogin.html', form=form, error=error)
    return redirect(url_for('main.auth.admin_login_form'))
