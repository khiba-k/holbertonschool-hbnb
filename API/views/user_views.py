#!/usr/bin/python3
from flask import Flask, requests,jsonify
from Model.user import User



def create_user():
    """Create new user
    """
    new_user = User(firstName=None, lastName=None, password=None, email=None)
    new_user.save_to_file()

def get_all_users():
    """Retrieve all existing users"""
    all_users = User.get_user()
    

def get_specific_user():
    """Get one place and return it"""

def update_user():
    pass

def delete_user():
    pass