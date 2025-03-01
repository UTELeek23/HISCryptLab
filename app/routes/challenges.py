from flask import Blueprint, jsonify, request
from app.models.challenge import Challenge
from app.utils.crypto import decrypt_aes

challenges_bp = Blueprint('challenges', __name__)

@challenges_bp.route('/challenges', methods=['GET'])
def get_challenges():
    challenges = Challenge.query.all()
    return jsonify([{'id': c.id, 'name': c.name, 'description': c.description} for c in challenges])

@challenges_bp.route('/decrypt/aes', methods=['POST'])
def decrypt_aes_route():
    data = request.json
    ciphertext = data['ciphertext']
    key = data['key']
    plaintext = decrypt_aes(ciphertext, key)
    return jsonify({'plaintext': plaintext})