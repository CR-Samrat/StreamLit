import streamlit as st
import pandas as pd
import numpy as np

# column attribute

# static image
col1,col2,col3 = st.columns(3)
with col1:
    st.header("Cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with col2:
    st.header("Dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with col3:
    st.header("Owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

# dynamic image
img_options = ['owl','cat','dog']
n = st.number_input("How many columns do you want :", min_value=1, max_value=50, value=1)
subject = st.selectbox("Select the image subject", img_options)
cols = st.columns(n)

for col in cols:
    with col:
        st.image("https://static.streamlit.io/examples/"+subject+".jpg", width=200)

# Tabs

#static tabs
tab1, tab2, tab3 = st.tabs(['Cat','Dog','Owl'])

with tab1:
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
    st.write("This is cat")
with tab2:
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
    st.write("This is dog")
with tab3:
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    st.write("This is owl")