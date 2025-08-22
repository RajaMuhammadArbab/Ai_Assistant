import wikipedia
from utils import get_time, get_math_result, set_reminder
import streamlit as st
import datetime

def handle_nlp_query(query):
    query = query.lower()

    if "time" in query or "date" in query:
        return get_time()
    elif any(op in query for op in ['+', '-', '*', '/']):
        return get_math_result(query)
    elif "remind me" in query:
        return set_reminder(query)
    elif any(greet in query for greet in ["hi", "hello", "hey"]):
        return "Hello! How can I assist you today?"
    else:
        try:
            return wikipedia.summary(query, sentences=2)
        except:
            return "Sorry, I couldn't find information on that topic."
   
