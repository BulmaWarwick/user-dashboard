import os
import sys
import logging
from flask import Flask, request, jsonify
from user_dashboard.models import User
from user_dashboard.utils import authenticate, authorize

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return jsonify([user.to_dict() for user in users])
    except Exception as e:
        logger.error(f"Error fetching users: {e}")
        return jsonify({"error": "Failed to fetch users"}), 500

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = User.query.get(user_id)
        if user is None:
            return jsonify({"error": "User not found"}), 404
        return jsonify(user.to_dict())
    except Exception as e:
        logger.error(f"Error fetching user: {e}")
        return jsonify({"error": "Failed to fetch user"}), 500

@app.route('/users', methods=['POST'])
@authenticate
@authorize
def create_user():
    try:
        data = request.json
        user = User(name=data['name'], email=data['email'])
        user.save()
        return jsonify(user.to_dict()), 201
    except Exception as e:
        logger.error(f"Error creating user: {e}")
        return jsonify({"error": "Failed to create user"}), 500

if __name__ == '__main__':
    app.run(debug=True)