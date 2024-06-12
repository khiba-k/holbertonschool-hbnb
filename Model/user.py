#!/usr/bin/python3
import uuid

class User:
    emails = []
    def __init__(self, firstName, lastName, password, email):
        self.user_id = uuid.uuid4().hex
        self.firstName =firstName
        self.lastName = lastName
        self.password = password
        self.email = email

    def add_email(self):
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
