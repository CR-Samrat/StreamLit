import streamlit as st
from PIL import Image

st.title("Image from Path")
st.image("./Data/Original_image.png")

st.title("Video from Path")
st.video("./Data/video.mp4")