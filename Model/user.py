#!/usr/bin/python3
import uuid

class User:
    def __init__(self, firstName, lastName, password, email):
        self.id = uuid.uuid4().hex
        self.firstName =firstName
        self.lastName = lastName
        self.password = password
        self.email = email

    def serialize(self):
        return {
            'id': self.id,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'password': self.password,
            'email': self.email 
        }
