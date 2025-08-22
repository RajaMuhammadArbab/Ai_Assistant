import streamlit as st
import pyrebase

def init_firebase():
    firebase_config = {
        "apiKey": "AIzaSyDvwdNzNOwUMNuWGmO7Ebl-rqlojk441ns",
        "authDomain": "ai-assistant-cfad5.firebaseapp.com",
        "projectId": "ai-assistant-cfad5",
        "storageBucket": "ai-assistant-cfad5.firebasestorage.app",
        "messagingSenderId": "704787367268",
        "appId": "1:704787367268:web:709d0e126b1886c70f6671",
        "measurementId": "G-T5P3RXKVQJ",
        "databaseURL": "https://your_project.firebaseio.com"

}
    st.session_state["firebase"] = pyrebase.initialize_app(firebase_config)


def login_ui():
    choice = st.sidebar.radio("Login or Guest", ["Login", "Guest"])
    if choice == "Login":
        email = st.sidebar.text_input("Email")
        password = st.sidebar.text_input("Password", type="password")
        if st.sidebar.button("Login"):
            try:
                auth = st.session_state["firebase"].auth()
                email = "arbab@gmail.com.com"
                password = "arbab786"
                user = auth.sign_in_with_email_and_password(email, password)
                user = auth.create_user_with_email_and_password(email, password)
                return user
                print("✅ Logged in:", user['email'])
            except:
                st.error("Login failed.")
    else:
        if st.sidebar.button("Continue as Guest"):
            st.session_state["guest_mode"] = True
            return None
