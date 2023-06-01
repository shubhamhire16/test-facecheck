import streamlit as st
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

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        query = {"username": username, "password": password}
        user = collection.find_one(query)
        if user:
            st.success("Logged in successfully!")
            
            
            
        else:
            st.error("Invalid username or password.")
