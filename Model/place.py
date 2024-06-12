#!/usr/bin/python3
from user import User
from country import Country
import uuid

class Place():
    taken_places = []
    def __init__(self, placeName, description, address, country_name, city_name, lattitude, 
                 longitude, numberOfRooms, bathrooms, 
                 pricePerNight, maxGuests):
        self.place_id = uuid.uuid4().hex
        self.placeName = placeName
        self.description = description
        self.address = address
        self.country = Country(country_name)
        self.city = city_name
        self.lattitude = lattitude
        self.longitude = longitude
        self.host = User.user_id
        self.numberOfRooms = numberOfRooms
        self.bathrooms = bathrooms
        self.pricePerNight = pricePerNight
        self.maxGuest =maxGuests
        self.amenities = []

    def add_place(self):
        if self.placeName not in Place.taken_places:
            Place.taken_places.append(self.placeName)
        return "Name is already taken"

"""
    @staticmethod
    def get_available_cities(country_name):
        country = Country(country_name)
        return country.get_cities()
"""

# Example usage:
if __name__ == "__main__":
    
    available_cities = Place.get_available_cities("United States")

    selected_city = available_cities[0]

    place = Place("Luxury Villa", "A beautiful villa with ocean view", 
                  "123 Ocean Drive", "United States", selected_city,
                  34.0522, -118.2437, 5, 3, 500, 10)

    print(f"Place: {place.placeName}")
    print(f"Description: {place.description}")
    print(f"Address: {place.address}")
    print(f"Country: {place.country.get_country_name()}")
    print(f"City: {place.city}")
    
