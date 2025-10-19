# app.py
import streamlit as st
from scraper import download_cause_lists # This imports your function from the other file

st.set_page_config(page_title="eCourts Scraper")

st.title("⚖️ Cause List Downloader")

st.markdown("Click the button to download all available cause lists for today from the **New Delhi District Court** website.")

# Create a button. The code inside this 'if' block will run when the button is clicked.
if st.button("Download All Cause Lists"):
    # Show a "spinner" message while the scraper is working
    with st.spinner("Working... A browser window will open and close automatically."):
        try:
            # This is where we call the function from scraper.py
            message = download_cause_lists()
            st.success(message) # Show a success message
            st.balloons()      # A fun little success animation
        except Exception as e:
            st.error(f"An error occurred: {e}") # Show an error if something goes wrong