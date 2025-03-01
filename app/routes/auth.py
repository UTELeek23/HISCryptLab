from flask import Blueprint, request, jsonify, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User
from app import db

# Tạo một Blueprint cho các route xác thực
auth_bp = Blueprint('auth', __name__)

# Route đăng ký
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Kiểm tra xem username đã tồn tại chưa
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists'}), 400

    # Tạo user mới
    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(username=username, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

# Route đăng nhập
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Tìm user trong database
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({'message': 'Invalid username or password'}), 401

    # Lưu thông tin user vào session
    session['user_id'] = user.id
    return jsonify({'message': 'Logged in successfully'}), 200

# Route đăng xuất
@auth_bp.route('/logout', methods=['POST'])
def logout():
    # Xóa thông tin user khỏi session
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully'}), 200

# Route lấy thông tin user hiện tại
@auth_bp.route('/me', methods=['GET'])
def get_current_user():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'message': 'Not logged in'}), 401

    user = User.query.get(user_id)
    return jsonify({'username': user.username}), 200