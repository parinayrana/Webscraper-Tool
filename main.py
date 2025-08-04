import streamlit as st
from scrape import (scrape_website,split_dom_content, clean_body_content, extract_body_content)

st.title("AI Webscraper")

url = st.text_input("Enter the website URL: ")

if st.button("Scrape Website"):
    st.write("Executing...")
    
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("VIEW DOM CONTENT"):
        st.text_area("DOM COntent", cleaned_content, height=300)


###