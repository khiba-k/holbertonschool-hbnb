#!/usr/bin/python3
"""Defines class for User entity"""
import uuid
from place import Place
import DataManager


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

    def __init__(self, firstName, lastName, password, email):
        """Method initializes the User Class instance

        Args:
            firstName (string): users first name
            lastName (string): users last name
            password (string): users password
            email (string): users email
        """

        self.user_id = uuid.uuid4().hex
        self.firstName =firstName
        self.lastName = lastName
        self.__password = password
        self.email = email

    def add_places(self):
        """Creates a list of places hosted by the user
        """
        if self.user_id == Place.host:
            User.user_places.append(Place.placeName)

    def add_user(self):
        """Creates a dictionery of the users information
        """
        User.user_details[self.user_id].append(self.firstName)
        User.user_details[self.user_id].append(self.lastName)
        User.user_details[self.user_id].append(self.__password)
        User.user_details[self.user_id].append(self.email)
        User.user_details[self.user_id].append(User.user_places)

        DataManager.save("user_details")

    def add_email(self):
        """Checks if email entered exists and adds it to list if not true 
        """
        if self.email not in User.emails:
            User.emails.append(self.email)
        return "Email already exists"
    
    


    def serialize(self):
        return {
            'user_id': self.user_id,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'password': self.password,
            'email': self.email 
        }



