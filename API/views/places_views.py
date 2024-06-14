from flask import Flask, requests
from Persistance import data_management as DM
from Model import place


def create_place(host_id,
              place_name=None, description=None, address=None,
              country_name=None, city_name=None, latitude=None,
              longitude=None, number_of_rooms=None, bathrooms=None,
              price_per_night=None, max_guests=None):
    """
    Add place to data structure and save it using DataManager.
    """

    place_obj = place.Place(host_id,
              place_name, description, address,
              country_name, city_name, latitude,
              longitude, number_of_rooms, bathrooms,
              price_per_night, max_guests)
    manipulate_data = DM.DataManager()

    place_data = manipulate_data.get("data_file.json", "places")
    if place_data is None:
        place_data["places"] = {}
    if place_obj.place_name not in place_data:
        data = dict(place_obj.to_dict)
        data["created_at"] = place_obj.stamps.created_at
        place_data[place_obj.place_name] = data
        manipulate_data.save(place_data, place_obj.host_id, place_obj.place_name)
        return "Place saved successfully."
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

