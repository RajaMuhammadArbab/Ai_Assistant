import streamlit as st
from nlp_module import handle_nlp_query
from data_analysis import data_analysis_ui
from prediction_module import prediction_ui
from firebase_auth import login_ui, init_firebase
from firebase_auth import init_firebase
from utils import greet_user
from PIL import Image
import warnings


warnings.filterwarnings("ignore")

col1, col2 = st.columns([1, 2])
with col1:
    st.set_page_config(page_title="AI Assistant", layout="centered") 
    st.title("💬 AI Assistant" ,width=1000)
    
with col2:
   
    image = Image.open("assets/assistant.png")  
    st.image(image, width=150 ,)    


init_firebase()

user = login_ui()
if user or st.session_state.get("guest_mode"):
    st.sidebar.success(f"Welcome, {user['email'] if user else 'Guest'}!")
   
    option = st.sidebar.selectbox("Choose an option", [
        "🤖 Chat Assistant", 
        "📊 Data Analysis", 
        "🔮 Predictive Modeling"
    ])

    if option == "🤖 Chat Assistant":
        greet_user()
        query = st.text_input("Ask me something:")
        if query:
            response = handle_nlp_query(query)
            st.write("💬", response)

    elif option == "📊 Data Analysis":
        data_analysis_ui()

    elif option == "🔮 Predictive Modeling":
        prediction_ui()
else:
    st.warning("Please log in or use guest mode to continue.")
