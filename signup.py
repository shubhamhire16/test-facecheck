
import streamlit as st
from pymongo import MongoClient
from bson.objectid import ObjectId


# Connection settings
MONGO_HOST = "localhost"
MONGO_PORT = 27017
MONGO_DB = "login_db"
MONGO_COLLECTION = "users"

# Create MongoDB client
client = MongoClient(host=MONGO_HOST, port=MONGO_PORT)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]

def signup():
    st.title("Sign Up")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        user_data = {
            "username": username,
            "password": password
        }
        collection.insert_one(user_data)
        st.success("Successfully signed up. Please log in.")