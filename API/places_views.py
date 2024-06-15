# from flask import Flask
from Persistance import data_management as DM
from Model import place
from flask import jsonify

manipulate_data = DM.DataManager()

def create_place(request_data):
    """
    Add place to data structure and save it using DataManager.

    Args:
        request_data (object): data from post method
    """

    place_obj = place.Place(request_data.get("host_id"),
              request_data.get("place_name"), request_data.get("description"),
              request_data.get("address"),
              request_data.get("country_name"), request_data.get("city_name"),
              request_data.get("latitude"),
              request_data.get("longitude"), request_data.get("number_of_rooms"),
              request_data.get("bathrooms"),
              request_data.get("price_per_night"), request_data.get("max_guests"), request_data.get("amenities"))
    data = place_obj.to_dict()
    # data["created_at"] = place_obj.created_at
    manipulate_data.save("places", data, place_obj.host_id, place_obj.place_name)
    manipulate_data.save("places", data)
    return "Place created successfully."
#############

def get_places():
    """Get all places function"""
    return jsonify(manipulate_data.get("places")), 200

def get_place(id):
    """Get one place and return it"""
    return jsonify(manipulate_data.get("places", id)), 200

def update_place():
    """update a spefic place"""
    pass

def delete_place(id):
    """delete a place"""

    return jsonify(delete_place("places", id)), 201
