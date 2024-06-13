from flask import Blueprint

bp = Blueprint('main', __name__)

# App index
@bp.route('/')
def home():
    return home()

# Users Routes
@bp.route('/users', method=['POST'])
def user():
    return create_user()

@bp.route('/users', method=['GET'])
def get_users():
    return get_all_users()

@bp.route('/users/<int:user_id>', method=['GET'])
def speicfic_user(user_id):
    return get_specific_user()

@bp.route('/users/<int:user_id>', method=['PUT'])
def up_user(user_id):
    return update_user()

@bp.route('/users/<int:user_id>', method=['DELETE'])
def del_user(user_id):
    return delete_user()


# Countries routes and paths
@bp.route('/countries', method=['GET'])
def user():
    return get_countries()

@bp.route('/countries/<country_code>', method=['GET'])
def user(country_code):
    return get_country()

@bp.route('/countries/<int:country_code/cities>', method=['GET'])
def user(country_code):
    return get_country_cities()

# City routes and paths

@bp.route('/cities', method=['POST'])
def city(user_id):
    return create_city()

@bp.route('/cities', method=['GET'])
def cities():
    return get_cities()

@bp.route('/cities/<int:city_id>', method=['GET'])
def retrieve_cities(city_id):
    return retrieve_city()

@bp.route('/cities/<int:city_id>', method=['PUT'])
def put_update_city():
    return update_city()

bp.route('/cities/<int:city_id>', method=['DELETE'])
def del_city():
    return delete_city()





