# Create Contact - POST
from flask import app, Blueprint, request, jsonify
from sqlalchemy import or_

from models.model import Contact, db, User

controller = Blueprint('controller', __name__)
app = controller

@app.route('/user/update', methods=['POST'])
def user_update():
    try:

        data = request.get_json()
        user = User.query.get_or_404(data['id'])
        user.name = data['name']
        user.mail = data['mail']
        user.phone = data['phone']
        user.address = data['address']

        db.session.commit()
        return jsonify({
            'message': 'Contact updated successfully',
            'contact': user.to_dict()
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()

        # Validate required fields
        required_fields = ['account', 'password']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({'error': f'Field {field} is required'}), 400

        exist = User.query.filter(
            or_(User.id == data['account'], User.name == data['account'], User.mail == data['account'], User.phone == data['account'])
        ).first()

        if not exist:
            return jsonify({'message': 'Login Error', 'code': 400}), 200

        if exist.password != data['password']:
            return jsonify({'message': 'Login Error', 'code': 400}), 200

        return jsonify({
            'message': 'Login Success',
            'contact': exist.to_dict()
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()

        # Validate required fields
        required_fields = ['name', 'mail', 'phone', 'address', 'password']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({'error': f'Field {field} is required'}), 400

        user = User(
            name=data['name'],
            mail=data['mail'],
            phone=data['phone'],
            address=data['address'],
            password=data['password']
        )

        db.session.add(user)
        db.session.commit()

        return jsonify({
            'message': 'Register Success',
            'contact': user.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/contacts', methods=['POST'])
def create_contact():
    try:
        data = request.get_json()

        # Validate required fields
        required_fields = ['name', 'mail', 'phone', 'address']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({'error': f'Field {field} is required'}), 400

        # Create new contact
        contact = Contact(
            name=data['name'],
            mail=data['mail'],
            phone=data['phone'],
            address=data['address']
        )

        db.session.add(contact)
        db.session.commit()

        return jsonify({
            'message': 'Contact created successfully',
            'contact': contact.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/contacts/uid', methods=['GET'])
def get_all_contacts_uid():
    try:
        uid = request.args.get('uid', '')
        user = User.query.filter(User.id == uid).first()
        if not user:
            return jsonify({'message': 'Uid does not exist', 'code': 400})

        contact = Contact(
            name=user.name,
            mail=user.mail,
            phone=user.phone,
            address=user.address
        )
        db.session.add(contact)
        db.session.commit()
        return jsonify({'message': 'Success', 'code': 200})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get All Contacts - GET
@app.route('/contacts', methods=['GET'])
def get_all_contacts():
    try:
        name_query = request.args.get('name', '')
        contacts = None
        if not name_query:
            contacts = Contact.query.all()
        else:
            contacts = Contact.query.filter(Contact.name.ilike(f'%{name_query}%')).all()

        return jsonify({
            'contacts': [contact.to_dict() for contact in contacts],
            'count': len(contacts)
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Update Contact - PUT
@app.route('/contacts/<int:id>', methods=['PUT'])
def update_contact(id):
    try:
        contact = Contact.query.get_or_404(id)
        data = request.get_json()

        # Update fields
        if 'name' in data:
            contact.name = data['name']
        if 'mail' in data:
            contact.mail = data['mail']
        if 'phone' in data:
            contact.phone = data['phone']
        if 'address' in data:
            contact.address = data['address']

        db.session.commit()

        return jsonify({
            'message': 'Contact updated successfully',
            'contact': contact.to_dict()
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Delete Contact - DELETE
@app.route('/contacts/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    try:
        contact = Contact.query.get_or_404(contact_id)

        db.session.delete(contact)
        db.session.commit()

        return jsonify({'message': 'Contact deleted successfully'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
