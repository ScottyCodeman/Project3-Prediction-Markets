import streamlit as st
from passlib.hash import pbkdf2_sha256
import os
from pymongo import MongoClient



class UserManager:
    def __init__(self):
        # Read configuration from .env file
        self.MONGO_URI = st.secrets['mongo_uri']
        self.client = MongoClient(self.MONGO_URI)
        self.db = self.client['my_database']
        self.users_collection = self.db['users']
        
    def set_authenticated(self, username, value):
        st.session_state[username + '_authenticated'] = value

    def is_authenticated(self, username):
        if username + '_authenticated' not in st.session_state:
            st.session_state[username + '_authenticated'] = False
        return st.session_state[username + '_authenticated']

    def register_user(self, username, password):
        user_data = self.users_collection.find_one({'username': username})
        if user_data:
            st.error("Username already exists. Please choose a different one.")
        else:
            password_hash = pbkdf2_sha256.hash(password)
            self.users_collection.insert_one({'username': username, 'password': password_hash,'admin': False})
            st.success("User registered successfully!")

    def login_user(self, username, password, session_state):
        user_data = self.users_collection.find_one({'username': username})
        if user_data:
            stored_password = user_data['password']
            if pbkdf2_sha256.verify(password, stored_password):
                st.success("Login successful!")
                st.session_state.authenticated = True  # Set the user as authenticated
            else:
                st.error("Invalid credentials. Please try again.")
        else:
            st.error("User not found. Please register first.")

    def logout(self):
        st.session_state["authenticated_user"] = None

    def update_chat_messages(job=None):
        chat_messages = user_manager.get_chat_messages()
        # You can then update the chat display with the new messages

    def store_chat_message(self, username, message):
        chat_message = {'username': username, 'message': message}
        self.db['chat_messages'].insert_one(chat_message)

    def get_chat_messages(self):
        chat_messages = self.db['chat_messages'].find()
        return chat_messages
        
    def clear_chat_messages(self):
        self.db['chat_messages'].delete_many({})

    def is_admin(self, username):
        user_data = self.users_collection.find_one({'username': username})
        if user_data and user_data.get('admin', False):
            return True
        else:
            return False
