import streamlit as st
from scrape import scrape_website

st.title("AI Webscraper")

url = st.text_input("Enter the website URL: ")

if st.button("Scrape Website"):
    st.write("Executing...")
    
#