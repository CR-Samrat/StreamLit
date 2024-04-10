import streamlit as st
import datetime

# add title
st.title("Hello There")

# headers -> header means sections
st.header("First Header")
st.header("Second Header")

#sub header -> means sub sections
st.subheader("First Sub Header")

#text
st.text("This is plain text")

#markdown -> Used to format plain text (Works same as jupiter markdown)
st.markdown("This is **Bold** text and this is *Italic*.")

# add python codes
st.write('range(1,10)')
st.write(list([1,2,3,4,5,6]))
st.write(i for i in range(1,10))

