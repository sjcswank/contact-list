import json

from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from .models import Contact
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
    contact_id = data['contactId']
    contact = Contact.query.get(contact_id)

    if contact:
        if contact.user_id == current_user.id:
            db.session.delete(contact)
            db.session.commit()
    return jsonify({})