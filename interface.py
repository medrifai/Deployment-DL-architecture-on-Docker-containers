import streamlit as st
import requests

st.title("Text Summarizer")

# Input text area
input_text = st.text_area("Enter text to summarize:", height=150)

if st.button("Summarize"):
    if input_text:
        # Make a request to the FastAPI service running in the inference container
        response = requests.post(f"http://inference:8000/summarize/", params={"text": input_text})
        if response.status_code == 200:
            summary = response.json().get("summary")
            st.subheader("Summary:")
            st.write(summary)
        else:
            st.write("Error in summarization.")
    else:
        st.write("Please enter some text to summarize.")