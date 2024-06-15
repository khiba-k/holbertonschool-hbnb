# from flask import Flask
from Persistance import data_management as DM
from Model import place


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
    manipulate_data = DM.DataManager()
    data = place_obj.to_dict()
    # data["created_at"] = place_obj.created_at
    manipulate_data.save("places", data, place_obj.host_id, place_obj.place_name)
    manipulate_data.save("places", data)
    return "Place created successfully."
#############

def get_places():
    """Get all places function"""
    pass

def get_place():
    """Get one place and return it"""
    pass

def update_place():
    pass

def delete_place():
    pass

def update_place():
    pass

def create_place_review():
    pass

def get_place_reviews_route():
    pass

