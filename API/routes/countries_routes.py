from flask import Blueprint
from views.countries_views import get_countries, get_country, get_country_cities, create_city, get_cities, retrieve_city, update_city, del_city

countries_bp = Blueprint('main', __name__)

# Countries routes and paths
@countries_bp.route('/countries', method=['GET'])
def countries_route():
    return get_countries()

@countries_bp.route('/countries/<int:country_code>', method=['GET'])
def get_country_route(country_code):
    return get_country()

@countries_bp.route('/countries/<int:country_code/cities>', method=['GET'])
def get_country_cities_route(country_code):
    return get_country_cities()

# City routes and paths

@countries_bp.route('/cities', method=['POST'])
def create_city_route(user_id):
    return create_city()

@countries_bp.route('/cities', method=['GET'])
def get_cities_route():
    return get_cities()

@countries_bp.route('/cities/<int:city_id>', method=['GET'])
def retrieve_city_route(city_id):
    return retrieve_city()

@countries_bp.route('/cities/<int:city_id>', method=['PUT'])
def update_city_route(city_id):
    return update_city()

@countries_bp.route('/cities/<int:city_id>', method=['DELETE'])
def del_city_route(city_id):
    return del_city()