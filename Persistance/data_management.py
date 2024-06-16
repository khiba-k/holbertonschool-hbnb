from Persistance.interface import IPersistenceManager
import json
import os

class DataManager(IPersistenceManager):
    """
    class for data management
    """

    def __init__(self, file_path="data_file.json"):
        self.file_path = file_path
        # Ensure the file exists
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump({
                    "users": {},
                    "countries": {},
                    "reviews": {},
                    "places": [],
                    "amenities": [],
                    "emails": {}
                }, file, indent=4)

    def save(self, entity_type, data, host_id=None, entity_id=None):
        """
        Save data to JSON file.

        Args:
            entity_type (string): Type of entity.
            data (object): Dictionary storing information.
            host_id (string): ID of host.
            entity_id (string): ID of entity.
        """
        try:
            with open("data_file.json", "r", encoding="utf-8") as file:
                file_data = json.load(file)

            if entity_type == "emails" and data in file_data["emails"].values():
                return "Email already exists"
                
            if host_id is not None and entity_id is not None:
                if host_id not in file_data["users"]:
                    if entity_type == "users":
                        file_data["users"][host_id] = {}
                    else:
                        return "Host does not exist"
                if entity_type not in file_data["users"][host_id]:
                    file_data["users"][host_id][entity_type] = {}
                file_data["users"][host_id][entity_type][entity_id] = data
            elif entity_id is not None:
                file_data[entity_type][entity_id] = data
            else:
                if entity_type in ["places", "amenities"]:
                    file_data[entity_type].append(data)

            with open("data_file.json", "w", encoding="utf-8") as file:
                json.dump(file_data, file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        return None
    

    def get(self, entity_type, entity_id=None, host_id=None):
        """
        Load information from data file.

        Args:
            entity_type (string): Type of entity (places, users, amenities, cities, or countries).
            entity_id (string): ID of places, users, amenities, cities, or countries.
            host_id (string): ID of host

        Returns:
            dict: Python dictionary of requested data.
        """
        try:
            with open("data_file.json", "r", encoding="utf-8") as file:
                data = json.load(file)
                if host_id is not None:
                    if entity_type in data["users"][host_id]:
                        if entity_id is not None:
                            return data["users"][host_id][entity_type].get(entity_id)
                        return data["users"][host_id]
                if entity_type in data:
                    if entity_id is not None:
                        if entity_type in ["places", "amenities"]:
                            for i in data[entity_type]:
                                if i.get("id") == entity_id:
                                    return i
                        elif entity_type == "email":
                            return data["email"]
                        return data[entity_type].get(entity_id)
                    return data.get(entity_type)
                return None
        except IOError as e:
            return f"Error loading data: {e}"
        except json.JSONDecodeError as e:
            return f"Error decoding JSON: {e}"


    def update(self,  entity_type, data, host_id=None, entity_id=None):
        """
        Update data in JSON file.

        Args:
            entity_type (string): Type of entity (places, users, amenities, cities, or countries).
            data (object): dictionary storing updated information
            host_id (string): id of host
            entity_id (string): ID of the entity to update.
            data (object): Updated information.
        """

        try:
            with open("data_file.json", "r", encoding="utf-8") as file:
                file_data = json.load(file)

            if host_id is not None and entity_id is not None:
                if host_id not in file_data["users"]:
                    return "Host does not exist"
                else:
                    if entity_type not in file_data["users"][host_id]:
                        return "Entity does not exist"
                    else:
                        file_data["users"][host_id][entity_type][entity_id] = data
            elif host_id is not None:
                file_data["users"][host_id] = data
            elif entity_type not in file_data:
                    return "Entity does does not exist"
            elif entity_id is not None:
                file_data[entity_type][entity_id] = data
            else:
                file_data[entity_type] = data

            with open("data_file.json", "w", encoding="utf-8") as file:
                json.dump(file_data, file, indent=4)
        except:
            return "something went wrong"
        return None
        

    def delete(self, entity_type, entity_id, host_id=None):
        """
        Delete information from JSON file.

        Args:
             entity_type (string): Type of entity (places, users, amenities, cities, or countries).
            entity_id (string): ID of the entity to delete.
            host_id (string): id of host
        """

        try:
            with open("data_file.json", "r", encoding="utf-8") as file:
                file_data = json.load(file)

            if host_id is not None:
                del file_data["users"][host_id][entity_type][entity_id]
            else:
                del file_data[entity_type][entity_id]
            
            with open("data_file.json", "w", encoding="utf-8") as file:
                json.dump(file_data, file, indent=4)
            return {"deleted": entity_id}
        except:
            return "something went wrong"
        return None
        