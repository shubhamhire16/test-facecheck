import streamlit as st
from pymongo import MongoClient
from bson.objectid import ObjectId
from signup import signup
from login import login

st.set_page_config(page_title = 'FaceCheck', layout='wide')

st.header('FaceCheck')

with st.spinner("Loading Models and Conneting to Redis db ..."):
    import face_rec
    


#localhost:27017
# Connection settings
MONGO_HOST = "localhost"
MONGO_PORT = 27017
MONGO_DB = "login_db"
MONGO_COLLECTION = "users"

# Create MongoDB client
client = MongoClient(host=MONGO_HOST, port=MONGO_PORT)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]

def main():
    
    with st.container():
    
        #st.markdown("<h1 style='text-align: center;'>Facecheck</h1>", unsafe_allow_html=True)
    # URL of the Lottie animation
        lottie_url = "https://embed.lottiefiles.com/animation/85293"

    # HTML code to embed the Lottie animation
        lottie_html = f'<iframe src="{lottie_url}" width="600" height="300" frameborder="0" style="border: none; padding-left:15%;text-align:center" ></iframe>'
    
    # Display the Lottie animation
        st.markdown(lottie_html, unsafe_allow_html=True)
        
        st.subheader("Please select an option:")
        page = st.radio("", ("Sign Up", "Login"))

        if page == "Sign Up":
            signup()
        elif page == "Login":
            login()

if __name__ == "__main__":
    main()


st.success('Model loaded sucesfully')
st.success('Redis db sucessfully connected')
