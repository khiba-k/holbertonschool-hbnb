#!/usr/bin/python3

"""
place.py is a module definig the Place class used for adding places
"""
from country import Country
import uuid

class Place():
    """
    Defines a place

    Attributes:
        available_places (object): stores places available for tenants 
    """
    available_places = {}
    def __init__(self, placeName=None, description=None, address=None, country_name=None, city_name=None, lattitude=None, 
                 longitude=None, numberOfRooms=None, bathrooms=None, 
                 pricePerNight=None, maxGuests=None):
        self.place_id = uuid.uuid4().hex
        self.placeName = placeName
        self.description = description
        self.address = address
        self.country = Country(country_name)
        self.city = city_name
        self.lattitude = lattitude
        self.longitude = longitude
        self.numberOfRooms = numberOfRooms
        self.bathrooms = bathrooms
        self.pricePerNight = pricePerNight
        self.maxGuest =maxGuests
        self.amenities = []

    def save_place(self):
        """
        add place to data structure
        """
        if self.placeName not in Place.available_places:
            data = dict((self.__dict__))
            del data["placeName"]
            Place.available_places[self.placeName] = data
            return
        return "Name is already taken"