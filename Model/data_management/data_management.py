from interface import IPersistenceManager
import json

class DataManager(IPersistenceManager):
    def save(self, entity):
        """
        Save data to JSON file.

        Args:
            entity (object): Dictionary storing information.
        """
        try:
            with open("data_file.json", "w", encoding="utf-8") as file:
                json.dump(entity, file)
        except IOError as e:
            print(f"Error saving data: {e}")

    def get(self, entity_id=None, entity_type=""):
        """
        Load information from data file.

        Args:
            entity_id (string): ID of places, users, amenities, cities, or countries.
            entity_type (string): Type of entity (places, users, amenities, cities, or countries).

        Returns:
            dict: Python dictionary of requested data.
        """
        try:
            with open("data_file.json", "r", encoding="utf-8") as file:
                data = json.load(file)
                if entity_type in data:
                    if entity_id is not None:
                        return data[entity_type].get(entity_id)
                    return data.get(entity_type)
                return None
        except IOError as e:
            print(f"Error loading data: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None

    def update(self, entity, entity_id, data):
        """
        Update data in JSON file.

        Args:
            entity (string): Type of entity (places, users, amenities, cities, or countries).
            entity_id (string): ID of the entity to update.
            data (object): Updated information.
        """
        try:
            with open("data_file.json", "r", encoding="utf-8") as file:
                file_data = json.load(file)
                if entity in file_data:
                    if entity_id in file_data[entity]:
                        file_data[entity][entity_id] = data

            with open("data_file.json", "w", encoding="utf-8") as file:
                json.dump(file_data, file)
        except IOError as e:
            print(f"Error updating data: {e}")

    def delete(self, entity_id, entity_type):
        """
        Delete information from JSON file.

        Args:
            entity_id (string): ID of the entity to delete.
            entity_type (string): Type of entity (places, users, amenities, cities, or countries).
        """
        try:
            with open("data_file.json", "r", encoding="utf-8") as file:
                data = json.load(file)
                if entity_type in data:
                    if entity_id in data[entity_type]:
                        del data[entity_type][entity_id]

            with open("data_file.json", "w", encoding="utf-8") as file:
                json.dump(data, file)
        except IOError as e:
            print(f"Error deleting data: {e}")
