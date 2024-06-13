from flask import Blueprint
from views.review_views import create_review_for_place, get_reviews_by_user, get_reviews_for_place, get_review, update_review, delete_review

review_bp = Blueprint('review', __name__)

@review_bp.route('/places/<int:place_id>/reviews', methods=['POST'])
def create_review_for_place_route(place_id):
    return create_review_for_place(place_id)

@review_bp.route('/users/<int:user_id>/reviews', methods=['GET'])
def get_reviews_by_user_route(user_id):
    return get_reviews_by_user(user_id)

@review_bp.route('/places/<int:place_id>/reviews', methods=['GET'])
def get_reviews_for_place_route(place_id):
    return get_reviews_for_place(place_id)

@review_bp.route('/reviews/<int:review_id>', methods=['GET'])
def get_review_route(review_id):
    return get_review(review_id)

@review_bp.route('/reviews/<int:review_id>', methods=['PUT'])
def update_review_route(review_id):
    return update_review(review_id)

@review_bp.route('/reviews/<int:review_id>', methods=['DELETE'])
def delete_review_route(review_id):
    return delete_review(review_id)
