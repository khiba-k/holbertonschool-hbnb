#!/usr/bin/python3
from place import Place

class Amenities(Place):
    def __init__(self, placeName, wifi, pool, extras=None):
        super().__init__(placeName)
        self.wifi = wifi
        self.pool = pool
        self.extras = [] if extras is None else extras
        

    def addExtras(self, *new_extras):
        self.extras.extend(new_extras)

if __name__ == "__main__":
    amenities = Amenities("Resort", True, True, ["Spa", "Gym"])
    print(amenities.extras)

    amenities.addExtras("Sauna", "Massage")
    print(amenities.extras)