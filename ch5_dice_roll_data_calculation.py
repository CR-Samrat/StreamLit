import streamlit as st
import numpy as np
import pandas as pd
import time

st.title("Dice Data Representation")

cases = []
for _ in range(100):
    cases.append(np.random.randint(1,7))

dataset = {}

for i in range(1,7):
    dataset[i] = cases.count(i)

with st.empty():
    st.write("You need to wait for 10 seconds")
    for seconds in range(10,0,-1):
        st.write("⌛",str(seconds),"seconds remaining")
        time.sleep(1)
    st.write("Chart is created")

st.bar_chart(data = dataset)

with st.expander("See Explaination"):
    st.write("The chart shows result by throwing a dice 100 times")
    st.image("https://static.streamlit.io/examples/dice.jpg")