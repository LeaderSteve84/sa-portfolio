#!/usr/bin/env python3
"""home module"""
from flask import Blueprint, request, render_template, redirect, url_for, \
    flash, jsonify, make_response, current_app
from flask_jwt_extended import create_access_token, set_access_cookies, \
    unset_jwt_cookies, jwt_required, get_jwt_identity
from app.forms.adminLogin import AdminLoginForm, AdminLogoutForm
from app.forms.forgotPassword import ForgotPasswordForm
from app.forms.resetPassword import ResetPasswordForm
from app.forms.changePassword import ChangePasswordForm
from app.models import Admin
from werkzeug.security import check_password_hash
from datetime import timedelta
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message
# from flask_wtf.csrf import CSRFProtect, csrf_exempt

auth_bp = Blueprint('auth', __name__)
mail = current_app.mail
db = current_app.db
csrf = current_app.csrf


@auth_bp.route("/login", methods=['GET', 'POST'], strict_slashes=False)
def login():
    """route to login"""
    form = AdminLoginForm()
    if form.validate_on_submit():
        username_email = form.username_email.data
        password = form.password.data
        admin = Admin.query.filter(
            (Admin.username == username_email)
            |
            (Admin.email == username_email)
        ).first()
        if admin and check_password_hash(admin.password_hash, password):
            access_token = create_access_token(
                identity=admin.id, expires_delta=timedelta(hours=1)
            )
            response = make_response(
                redirect(url_for('main.admindashboard.admindashboard_page'))
            )
            set_access_cookies(response, access_token)
            return response
        else:
            flash('Invalid username/email or password', 'error')
    else:
        if form.errors != {}:
            for error_message in form.errors.values():
                flash(f"login not successful: {error_message}", "error")
    return render_template('adminlogin.html', form=form)


@auth_bp.route("/logout-form", methods=['GET'], strict_slashes=False)
def logoutForm():
    """logout page"""
    form = AdminLogoutForm()
    return render_template('logout.html', form=form)


@auth_bp.route("/logout", methods=['POST'], strict_slashes=False)
def logout():
    """route to handle admin logout"""
    form = AdminLogoutForm()
    if form.validate_on_submit:
        response = make_response(redirect(url_for('main.home.home_page')))
        # unset the JWT cookies to log out
        unset_jwt_cookies(response)
        flash("log out successfully", "success")
        return response
    else:
        if form.errors != {}:
            for error_message in form.errors.values():
                flash(f"logout not successful: {error_message}", "error")
                return redirect(url_for("main.auth.logoutForm"))


def generate_reset_token(email):
    """to generate the reset token"""
    s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    return s.dumps(email, salt='password-reset-salt')


def verify_reset_token(token, expiration=3600):
    """to verify reset token"""
    s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    try:
        email = s.loads(token, salt="password-reset-salt", max_age=expiration)
    except exception as e:
        return None
    return email


def send_reset_email(admin_email, token):
    """send reset email"""
    msg = Message(
        subject='Password Reset Request',
        recipients=[admin_email]
    )
    reset_url = url_for(
        'main.auth.reset_password', token=token, _external=True
    )
    msg.body = f'''To reset your password, visit the following link:
    {reset_url}
    If you did not make this request, simply ignore this email.
    '''
    mail.send(msg)


@auth_bp.route("/forgot_password", methods=['GET', 'POST'])
def forgot_password():
    """forgot password routes"""
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(email=form.email.data).first()
        if admin:
            token = generate_reset_token(admin.email)
            send_reset_email(admin.email, token)
            flash('password reset email has been sent', 'info')
        else:
            flash('No account found with that email.', 'warning')
            return render_template('forgot_password.html', form=form)
    else:
        if form.errors != {}:
            for error_message in form.errors.values():
                flash(f"Error validating your email: {error_message}", "error")
    return render_template('forgot_password.html', form=form)


@auth_bp.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_password(token):
    """reset the password"""
    email = verify_reset_token(token)
    if email is None:
        flash('The token is either invalid or expired', 'danger')
        return redirect(url_for('main.auth.forgot_password'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(email=email).first()
        if admin:
            admin.set_password(form.password.data)
            db.session.commit()
            flash('Your password has been reset!', 'success')
            return redirect(url_for('main.auth.login'))
    return render_template('reset_password.html', form=form, token=token)


@auth_bp.route("/change_password", methods=['GET'])
@jwt_required()
def change_password_page():
    """return admin change password form"""
    admin_id = get_jwt_identity()
    admin = Admin.query.filter_by(id=admin_id).first()
    print(admin.id)
    if not admin:
        flash('You are not an admin', 'warning')
        return redirect(url_for('main.home.home_page'))
    form = ChangePasswordForm()
    return render_template('change_password.html', form=form, admin=admin)


@auth_bp.route("/change_password/<string:admin_id>/update", methods=['POST'])
def change_password(admin_id):
    """to change admin password"""
    form = ChangePasswordForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(id=admin_id).first()
        if admin:
            old_password = form.old_password.data
            new_password = form.new_password.data
            # check if old password is correct
            if not check_password_hash(admin.password_hash, old_password):
                flash('Incorrect current password', 'warning')
                return render_template(
                    'change_password.html', form=form, admin=admin
                )
            admin.set_password(new_password)
            db.session.commit()
            flash('Admin password updated successfully', 'success')
            return redirect(url_for('main.admindashboard.admindashboard_page'))
    else:
        if form.errors != {}:
            for error_message in form.errors.values():
                flash(
                    f"Error changing your password: {error_message}", "error"
                )
                return redirect(url_for('main.auth.change_password_page'))
