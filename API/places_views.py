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
              request_data.get("price_per_night"), request_data.get("max_guests"))
    manipulate_data = DM.DataManager()

    place_data = manipulate_data.get("data_file.json", "places")
    if place_data is None:
        place_data["places"] = {}
    if place_obj.place_name not in place_data:
        data = dict(place_obj.to_dict)
        data["created_at"] = place_obj.stamps.created_at
        place_data[place_obj.place_name] = data
        manipulate_data.save(place_data, place_obj.host_id, place_obj.place_name)
        return "Place creater successfully."
    return "Place name is already taken."

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

