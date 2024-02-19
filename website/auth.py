from flask import Blueprint, request, flash, render_template


auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return "<h1>Login Page</h1>"


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
            flash('User Created!', category='success')
    return render_template('sign-up.html')


@auth.route('/logout')
def logout():
    return "<h1>Logout Page</h1>"
