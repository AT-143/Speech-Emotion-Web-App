import numpy as np
import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
import os
from datetime import datetime

starttime = datetime.now()
# page settings
st.set_page_config(layout="wide")

max_width = 1000
padding_top = 0
padding_right = "20%"
padding_left = "10%"
padding_bottom = 0
COLOR = "#1f1f2e"
BACKGROUND_COLOR = "#d1d1e0"

st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: {max_width}px;
        padding-top: {padding_top}rem;
        padding-right: {padding_right}rem;
        padding-left: {padding_left}rem;
        padding-bottom: {padding_bottom}rem;
    }}
    .reportview-container .main {{
        color: {COLOR};
        background-color: {BACKGROUND_COLOR};
    }}
</style>
""",
        unsafe_allow_html=True,
    )

@st.cache
def log_file():
    with open(os.path.join("test1.txt"), "a") as f:
        txt = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        f.write(f"{txt};\n")

@st.cache
def load_file():
    starttime = datetime.now()
    try:
        with st.spinner('Wait for it...'):
            st.text("Model is loading...")
            model = tf.keras.models.load_model("archive/model2.h5")
        st.success("Done!")
    except Exception as ex:
        st.write("Error: model #1 is not loaded")
        st.write(ex)
    try:
        with st.spinner('Wait for it...'):
            st.text("Model is loading...")
            tmodel = load_model("tmodel_all.h5")
        st.success("Done!")
    except Exception as ex:
        st.write("Error: model #2 is not loaded")
        st.write(ex)
    endtime = datetime.now() - starttime
    st.markdown(f"### Loading time: {endtime}")


if __name__ == '__main__':
    st.title("Hello world")
    user_input = st.text_area("label goes here")

    if st.button("loadfile"):
        load_file()
        st.success("yeah!")

    if st.button("logfile"):
        log_file()
        st.success("yeah!")