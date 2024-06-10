#!/usr/bin/python3

class Country:
    def __init__(self, country_name):
        self.country = country_name
        self.cities = []

    def add_city(self, city_name):
        if city_name not in self.cities:
            self.cities.append(city_name)

    def get_cities(self):
        return self.cities

    def get_country_name(self):
        return self.country

# Example usage
if __name__ == "__main__":
    lesotho = Country("Lesotho")
    south_africa = Country("South Africa")

    lesotho.add_city("Maseru")
    lesotho.add_city("Hlotse")
    lesotho.add_city("Pitseng")

    south_africa.add_city("Cape Town")
    south_africa.add_city("Durban")
    south_africa.add_city("East London")

    print(f"Country: {lesotho.country}")
    print("Cities:")
    for city in lesotho.cities:
        pass
        print(f"- {city}")

    print(f"Country: {south_africa.country}")
    print("Cities:")
    for city in south_africa.cities:
        pass
        print(f"- {city}")
