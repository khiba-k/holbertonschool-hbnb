#!/usr/bin/python3
"""Defines class for User entity"""
import uuid
from place import Place
from base_model import BaseModel


class User:
    """Handles the users information
    Attributes:
        emails []: Has all the existing emails in the system
        user_places []: Has list of the places the user is hosting
        user_details {}: Dictionery containing users information 
    """

    emails = []
    user_places = []
    user_details = {}
    users = {}
    data = []

    def __init__(self, firstName, lastName, password, email):
        """Method initializes the User Class instance

        Args:
            firstName (string): users first name
            lastName (string): users last name
            password (string): users password
            email (string): users email
        """

        self.user_id = uuid.uuid4().hex
        self.firstName = firstName
        self.lastName = lastName
        self.__password = password
        self.email = email
        self.created_at = BaseModel.save()



    def add_places(self):
        """Creates a list of places hosted by the user
        """
        if self.user_id == Place.host:
            User.user_places.append(Place.placeName)
        
    def add_email(self):
        """Checks if email entered exists and adds it to list if not true 
        """
        if self.email not in User.emails:
            User.emails.append(self.email)
        return "Email already exists"
    
    def to_dict(self):
        """Creates a list of all users
        """
        
        data = {
            "first_name": self.firstName,
            "last_name": self.lastName,
            "email": self.lastName,
            "password": self.__password,
            "places": User.user_places,
            "created_at": self.created_at
        }
        User.users[self.user_id] = data

        return User.users
    

