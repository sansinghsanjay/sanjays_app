# python imports
import os
import json
import streamlit as st

# utils imports
from utils.timestamp import get_current_timestamp
from utils.logger import log_status

# modules imports

# paths
config_json_path = os.path.abspath("./config.json")

# load config params
log_status(status="INFO", source="/app.py", timestamp=get_current_timestamp(), msg="Loading config params")
f_ptr = open(config_json_path, "rb")
config = json.load(f_ptr)
f_ptr.close()

# configure the streamlit page
st.set_page_config(layout="wide")
st.markdown(
    body="""
        <style>
            .block-container{
                    padding-top: 20px;
                }
        </style>
    """, 
    unsafe_allow_html=True
)

# app title
st.title(config["app_title"])

# app header
st.header(config["app_header"])

# text input
first_name = st.text_input(label="Enter your first name", placeholder="First Name")

# button
if(st.button(label="Say hi to me!")):
    st.toast(body=f"Hi {first_name}!", icon="👋", duration="short")
