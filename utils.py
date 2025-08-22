from datetime import datetime
import re
import streamlit as st

def greet_user():
    hour = datetime.now().hour
    if hour < 12:
        greeting = "Good Morning!"
    elif hour < 18:
        greeting = "Good Afternoon!"
    else:
        greeting = "Good Evening!"
    st.write(f"👋 {greeting}")

def get_time():
    now = datetime.now()
    return f"The current date and time is {now.strftime('%Y-%m-%d %H:%M:%S')}"

def get_math_result(query):
    try:
        result = eval(query)
        return f"The result is {result}"
    except:
        return "Sorry, I couldn't evaluate the expression."

def set_reminder(query):
    return "🔔 Reminder has been set! (This is a placeholder implementation.)"
