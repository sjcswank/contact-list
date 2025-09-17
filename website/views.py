import json

from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from flask_login import login_required, current_user, logout_user
from .models import Contact, User
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        address = request.form.get('address')

        new_contact = Contact(name=name, email=email, phone=phone, address=address, user_id=current_user.id)
        db.session.add(new_contact)
        db.session.commit()

    return render_template('home.html', user=current_user)


@views.route('/delete-contact', methods=['POST'])
def delete_contact():
    data = json.loads(request.data)
    print(data)
    contact_id = data['contactId']
    contact = Contact.query.get(contact_id)

    if contact:
        if contact.user_id == current_user.id:
            db.session.delete(contact)
            db.session.commit()
    return jsonify({})


@views.route('/edit-contact', methods=['GET', 'POST'])
@login_required
def edit_contact():
    id = request.args.get('contact_id')
    contact = Contact.query.get(id)

    if request.method == 'POST':
        contact.name = request.form.get('name')
        contact.email = request.form.get('email')
        contact.phone = request.form.get('phone')
        contact.address = request.form.get('address')

        db.session.commit()
        return redirect(url_for('views.home'))

    return render_template('edit.html', contact=contact, user=current_user)


@views.route('/delete-user', methods=['POST'])
def delete_user():
    data = json.loads(request.data)
    print(data)
    user_id = data['userId']
    user = User.query.get(user_id)

    if user:
        db.session.delete(user)
        db.session.commit()
    else:
        return jsonify({ "Status": 204 })
    return jsonify({ "Status": 200 })