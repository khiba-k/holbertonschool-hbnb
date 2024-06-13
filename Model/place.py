from country import Country
from base_model import BaseModel

"""
defines a place class
"""

class Place:
    """
    Defines a place.
    """

    def __init__(self, host_id: str, place_name: str = None, description: str = None, 
                 address: str = None, country_name: str = None, city_name: str = None, 
                 latitude: float = None, longitude: float = None, number_of_rooms: int = None, 
                 bathrooms: int = None, price_per_night: float = None, max_guests: int = None):
        self.stamps = BaseModel()
        self.place_id = self.stamps.id
        self.place_name = place_name
        self.description = description
        self.address = address
        self.host_id = host_id
        self.country = Country(country_name)
        self.city = city_name
        self.latitude = latitude
        self.longitude = longitude
        self.number_of_rooms = number_of_rooms
        self.bathrooms = bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.amenities = []