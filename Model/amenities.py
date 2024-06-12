#!/usr/bin/python3
from place import Place
from user import User

class Amenities(Place):
    def __init__(self, placeName, wifi, pool, extras=None):
        self.wifi = wifi
        self.pool = pool
        self.extras = [] if extras is None else extras
        
        # place = Place.taken_places[User.users[placeName[id]]]
        # place[amenities] = {
        #     wifi: None,
        #     pool: True, 
        #     extras: extras
        # }

    def addExtras(self, *new_extras):
        self.extras.extend(new_extras)

if __name__ == "__main__":
    amenities = Amenities("Resort", True, True, ["Spa", "Gym"])
    print(amenities.extras)

    amenities.addExtras("Sauna", "Massage")
    print(amenities.extras)
