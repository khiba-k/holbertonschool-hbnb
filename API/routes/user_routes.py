from flask import Blueprint
from views.user_views import create_user, get_all_users, get_specific_user, update_user, delete_user

user_bp = Blueprint('main', __name__)

# App index
@user_bp.route('/')
def home():
    return home()

# Users Routes
@user_bp.route('/users', method=['POST'])
def user():
    return create_user()

@user_bp.route('/users', method=['GET'])
def get_users():
    return get_all_users()

@user_bp.route('/users/<int:user_id>', method=['GET'])
def speicfic_user(user_id):
    return get_specific_user(user_id)

@user_bp.route('/users/<int:user_id>', method=['PUT'])
def up_user(user_id):
    return update_user(user_id)

@user_bp.route('/users/<int:user_id>', method=['DELETE'])
def del_user(user_id):
    return delete_user(user_id)





