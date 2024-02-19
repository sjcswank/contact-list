from flask import Blueprint, request, flash, render_template
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                flash('Logged in successfully!', category='success')
            else:
                flash('Incorrect Password.', category='error')
        else:
            flash('Incorrect email', category='error')

    return render_template('login.html')


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password1')
        confirm_password = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be more than 3 characters.', category='error')
        elif len(password) < 7:
            flash('Password must at least 7 characters long.', category='error')
        elif password != confirm_password:
            flash('Passwords do not match.', category='error')
        else:
            new_user = User(email=email, password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('User Created!', category='success')
    return render_template('sign-up.html')


@auth.route('/logout')
def logout():
    return "<h1>Logout Page</h1>"
