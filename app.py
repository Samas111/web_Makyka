import filecmp
import streamlit as st 
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import pandas as pd

st.set_page_config(page_title="Makyka Web (Test)", page_icon=":computer:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()