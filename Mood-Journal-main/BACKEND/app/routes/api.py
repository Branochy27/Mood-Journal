from flask import Blueprint

# Create the blueprint
api_bp = Blueprint('api', __name__)

# Health check route
@api_bp.route('/ping', methods=['GET'])
def ping():
    return {'message': 'pong'}, 200