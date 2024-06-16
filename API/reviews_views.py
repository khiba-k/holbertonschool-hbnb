from flask import Flask, request, jsonify, abort
from Model.place import Place
from Model.review import Review
from Model.user import User
from Persistance.data_management import DataManager
from datetime import datetime



entity_type = "reviews"
data_manager = DataManager()

def create_review_for_place(review_data, place_id):
    """Create a new review for a place"""
    data = request.json
    user_id = data.get('user_id')
    rating = data.get('rating')
    comment = data.get('comment')

    # Validate input
    if not (user_id and rating and comment):
        abort(400, 'Missing required fields')

    # Validate rating
    if rating not in range(1, 6):
        abort(400, 'Rating must be between 1 and 5')

    # Check if user and place exist
    if not data_manager.get('users', user_id):
        abort(404, f'User with ID {user_id} not found')
    if not data_manager.get('places', place_id):
        abort(404, f'Place with ID {place_id} not found')

    # Additional business logic to prevent hosts from reviewing their own place goes here
    # Assuming such logic is implemented in the data manager or elsewhere

    # Create review object
    review = {
        'place_id': place_id,
        'user_id': user_id,
        'rating': rating,
        'comment': comment,
        'created_at': datetime.now(),
        'updated_at': None  # To be updated on modification
    }

    # Save review
    review_id = data_manager.save('reviews', review)

    data_manager.save(entity_type, review_id)
    data_manager.save(entity_type, review_id)

    return jsonify(review), 201


def get_reviews_by_user():
    """Retrieve all reviews written by a specific user"""
    reviews = [review for review in data_manager.get('reviews').values() if review['user_id'] == user_id]
    if not reviews:
        abort(404, f'No reviews found for user ID {user_id}')

    return jsonify(reviews), 200

def get_reviews_for_place():
    pass

def get_review(self, review_id):
    review = data_manager.get('reviews', review_id)
    if not review:
        abort(404, f'Review with ID {review_id} not found')

    return jsonify(review), 200

def update_review(self, review_id):
    # Validate input
    if not (user_id and rating and comment):
        abort(400, 'Missing required fields')

    # Validate rating
    if rating not in range(1, 6):
        abort(400, 'Rating must be between 1 and 5')

    # Check if review exists
    review = data_manager.get('reviews', review_id)
    if not review:
        abort(404, f'Review with ID {review_id} not found')

    # Ensure user cannot update other user's reviews (if such logic applies)
    if review['user_id'] != user_id:
        abort(403, 'You are not allowed to update this review')

    # Update review object
    review.update({
        'rating': rating,
        'comment': comment,
        'updated_at': datetime.utcnow().isoformat()
    })

    # Save updated review
    data_manager.update('reviews', review_id, review)

    return jsonify(review), 200
def delete_review(self, review_id):
    """Delete a specific review"""
    review = data_manager.get('reviews', review_id)
    if not review:
        abort(404, f'Review with ID {review_id} not found')

    data_manager.delete('reviews', review_id)

    return '', 204


    data_ma
