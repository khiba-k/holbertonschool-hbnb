#!/usr/bin/python3
"""Defines class for User entity"""
import uuid
# from Model.place import Place
from base_model import BaseModel
from Persistance.data_management import DataManager


class User:
    """Handles the users information

    Attributes:
        emails []: Has all the existing emails in the system
        user_places []: Has list of the places the user is hosting
        user_details {}: Dictionery containing users information 
    """

    emails = []
    user_places = []
    users = {}

    def __init__(self, firstName, lastName, password, email):
        """Method initializes the User Class instance

        Args:
            firstName (string): users first name
            lastName (string): users last name
            password (string): users password
            email (string): users email
        """

        self.stamps = BaseModel()
        self.user_id = self.stamps.id
        self.firstName = firstName
        self.lastName = lastName
        self.__password = password
        self.email = email
        self.created_at = str(self.stamps.created_at)
    
    def to_dict(self):
        """Creates a dictionary of all users
        """
        
        data = {
            "first_name": self.firstName,
            "last_name": self.lastName,
            "email": self.email,
            "password": self.__password,
            "created_at": self.created_at
        }
        return data
    
    def save_to_file(self):
        """Saves user information to json file
        """
        
        data_manager = DataManager()
        data_manager.save("emails", self.email, None,  self.user_id)
        data_manager.save("users", self.to_dict(), None, self.user_id)
    
    # def get_user(self):
    #     """Retrieve user information from json file
    #     """
    #     data_manager = DataManager()
    #     user_data = data_manager.get("users", self.user_id)
    #     if user_data:
    #         print(json.dumps(user_data, indent=4))
    #     else:
    #         print("User not found")


    def user_update(self):
        """Update user information in json file
        """
        data_manager = DataManager()
        data_manager.update("users", self.to_dict(), None, self.user_id)

    def delete_user(self):
        """Deletes user information from json file
        """
        data_management = DataManager()
        data_management.delete("users", self.user_id)
        data_management.delete("emails", self.user_id)

    

