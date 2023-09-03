import streamlit as st
import json
import requests

# Define the endpoint of the FastAPI application
endpoint = "https://aastroza--example-fastapi-app-fastapi-app-dev.modal.run/campaign"

# Set the title of the Streamlit application
st.title("Marketing Campaign Generator 🔥")

# Create a text area for the user to input their brand name and a short description of their brand
prompt = st.text_area("Enter your brand name and a short description of your brand. We will generate a marketing campaign for you 🚀.")

# Prepare the input data for the API request
input_data = {"prompt": prompt}

# If the "Generate" button is clicked, send a request to the FastAPI application and display the response
if st.button("Generate"):
    if not prompt:
        st.warning("Please enter your brand name and description.")
    else:
        try:
            res = requests.post(url=endpoint, data=json.dumps(input_data))
            if res.status_code == 200:
                res_json = res.json()
                st.subheader("Generated Campaign")
                st.markdown(res_json["campaign_text"])
            else:
                st.error(f"Error: {res.status_code} - {res.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")
