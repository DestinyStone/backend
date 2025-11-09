# Create Contact - POST
import jwt
from flask import app, Blueprint, request, jsonify
from sqlalchemy import or_

from models.model import Contact, db, User

controller = Blueprint('controller', __name__)
app = controller

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()

    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists'}), 400

    hashed_password = data['password']
    new_user = User(
        username=data['username'],
        password=hashed_password,
        nickname=data['nickname'],
        realname=data['realname']
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()

    if user and user.password == data['password']:
        return jsonify({
            'message': 'Login successful',
            'user': {
                'id': user.id,
                'username': user.username,
                'nickname': user.nickname,
                'realname': user.realname
            }
        }), 200

    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/api/profile/<int:user_id>', methods=['PUT'])
def update_profile(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    data = request.get_json()
    user.nickname = data.get('nickname', user.nickname)
    user.realname = data.get('realname', user.realname)

    if 'password' in data and data['password']:
        user.password = data['password']

    db.session.commit()

    return jsonify({'message': 'Profile updated successfully'}), 200

# Contact routes
@app.route('/api/contacts', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    return jsonify([{
        'id': contact.id,
        'name': contact.name,
        'phone': contact.phone,
        'email': contact.email,
        'gender': contact.gender,
        'age': contact.age
    } for contact in contacts])

@app.route('/api/contacts', methods=['POST'])
def add_contact():
    data = request.get_json()
    new_contact = Contact(
        name=data['name'],
        phone=data['phone'],
        email=data['email'],
        gender=data['gender'],
        age=data['age']
    )

    db.session.add(new_contact)
    db.session.commit()

    return jsonify({'message': 'Contact added successfully'}), 201

@app.route('/api/contacts/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    contact = Contact.query.get(contact_id)
    if not contact:
        return jsonify({'message': 'Contact not found'}), 404

    data = request.get_json()
    contact.name = data.get('name', contact.name)
    contact.phone = data.get('phone', contact.phone)
    contact.email = data.get('email', contact.email)
    contact.gender = data.get('gender', contact.gender)
    contact.age = data.get('age', contact.age)

    db.session.commit()

    return jsonify({'message': 'Contact updated successfully'}), 200

@app.route('/api/contacts/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    contact = Contact.query.get(contact_id)
    if not contact:
        return jsonify({'message': 'Contact not found'}), 404

    db.session.delete(contact)
    db.session.commit()

    return jsonify({'message': 'Contact deleted successfully'}), 200
