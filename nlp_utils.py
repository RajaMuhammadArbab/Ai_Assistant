import datetime
import wikipedia

def process_query(query):
    query = query.lower()

    if "hello" in query or "hi" in query:
        return "Hello! How can I assist you today?"
    
    elif "time" in query:
        return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"

    elif "date" in query:
        return f"Today's date is {datetime.datetime.now().strftime('%A, %B %d, %Y')}"

    elif "calculate" in query:
        try:
            expression = query.split("calculate")[-1]
            result = eval(expression)
            return f"The result is {result}"
        except:
            return "Sorry, I couldn't calculate that. Please try again with a valid expression."

    else:
        try:
            return wikipedia.summary(query, sentences=2)
        except:
            return "Sorry, I couldn't find anything related to that topic."
