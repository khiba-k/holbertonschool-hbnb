from flask import Blueprint
from views.places_views import create_place, get_places, get_place, update_place, delete_place, create_place_review, get_place_reviews

places_bp = Blueprint('places', __name__)

@places_bp.route('/places', methods=['POST'])
def create_place_route():
    return create_place()

@places_bp.route('/places', methods=['GET'])
def get_places_route():
    return get_places()

@places_bp.route('/places/<int:place_id>', methods=['GET'])
def get_place_route(place_id):
    return get_place(place_id)

@places_bp.route('/places/<int:place_id>', methods=['PUT'])
def update_place_route(place_id):
    return update_place(place_id)

@places_bp.route('/places/<int:place_id>', methods=['DELETE'])
def delete_place_route(place_id):
    return delete_place(place_id)

@places_bp.route('/places/<int:place_id>/reviews', methods=['POST'])
def create_place_review_route(place_id):
    return create_place_review(place_id)

@places_bp.route('/places/<int:place_id>/reviews', methods=['GET'])
def get_place_reviews_route(place_id):
    return get_place_reviews(place_id)
