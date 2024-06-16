from flask import Flask, request, jsonify
from Model.place import Place
from Model.review import Review
from Model.user import User
from Persistance.data_management import DataManager


manipulate_data = DataManager()
entity_type = "reviews"


def create_review(req_data):
    """
    Add review to data structure and save it using DataManager.
    """
    try:
        request_data = req_data
        required_fields = ["user_id", "place_id", "comment", "ratings"]

        for field in required_fields:
            if field not in request_data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        user_id = request_data.get("user_id")
        place_id = request_data.get("place_id")

        # Retrieve user and place data
        user = manipulate_data.get("users", user_id)
        place = manipulate_data.get("list_of_places", place_id)

        if not user:
            return jsonify({'error': 'Invalid user'}), 400
        if not place:
            return jsonify({'error': 'Invalid place'}), 400

        review_obj = Review(
            user=user,
            place=place,
            comment=request_data.get("comment"),
            ratings=request_data.get("ratings")
        )

        review_data = review_obj.to_dict()
        manipulate_data.save(entity_type, review_data, review_obj.user_id, review_obj.id)

        return jsonify({"message": "Review created successfully."}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


def create_review_for_place(place_id):
    review_data = request.get_json()
    review_data['place_id'] = place_id
    return create_review(review_data)


def get_reviews_by_user():
    pass

def get_reviews_for_place():
    pass

def get_review():
    pass

def update_review():
    pass

def delete_review():
    pass


    data_ma
