from flask import Blueprint
from views.amenities_views import create_amenity, get_amenities, get_amenity, update_amenity, delete_amenity

amenities_bp = Blueprint('amenities', __name__)

@amenities_bp.route('/amenities', methods=['POST'])
def create_amenity_route():
    return create_amenity()

@amenities_bp.route('/amenities', methods=['GET'])
def get_amenities_route():
    return get_amenities()

@amenities_bp.route('/amenities/<int:amenity_id>', methods=['GET'])
def get_amenity_route(amenity_id):
    return get_amenity(amenity_id)

@amenities_bp.route('/amenities/<int:amenity_id>', methods=['PUT'])
def update_amenity_route(amenity_id):
    return update_amenity(amenity_id)

@amenities_bp.route('/amenities/<int:amenity_id>', methods=['DELETE'])
def delete_amenity_route(amenity_id):
    return delete_amenity(amenity_id)
