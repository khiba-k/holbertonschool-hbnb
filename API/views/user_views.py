from flask import Flask, requests,jsonify
from Persistance.data_management import DataManager
from Model.user import User


users = User.all_users
user_id = User.all_users

def create_user():
    pass 

def get_all_users():
    """Get all places function"""
    DataManager.get(users)
    return jsonify(users)

def get_specific_user():
    """Get one place and return it"""
    DataManager.get(users, user_id)

def update_user():
    pass

def delete_user():
    pass