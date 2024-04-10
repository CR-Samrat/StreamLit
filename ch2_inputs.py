import streamlit as st
import datetime

st.title("Taking input in Streamlit")

# taking text input
name = st.text_input('Enter your name:')
st.write("Hello",name)

# taking large input
comment = st.text_area('Enter your feedback:')
st.write("Thanks for you feedback -",comment)

# taking number input
age = st.number_input("Enter your age",min_value=18, max_value=120, value=30)
st.write("Your age is",age)

# taking date input
dob = st.date_input("Enter your date of birth :",value=datetime.date(2000, 1, 1), min_value=datetime.date(1990,1,1), max_value=datetime.date.today())
st.write("Your date of birth :",dob)

# dropdown input
gender_options = ['Male','Female','Other']
gender = st.selectbox("Select your gender :",gender_options)
st.write("You are",gender)

# radio button
passport = st.radio("Do you have any passport", options=('Yes','No, but i have applied for it','No'), help='Choose one', horizontal=True)
st.write("You have selected", passport)

# multiple select box
skills = st.multiselect("Select yours skills", options=("C","Java","Python","React","Machine Learning","Blockchain","Cybersecurity"))
st.write("Your skills are",skills)

# button
if st.button('Say Hello'):
    st.write("Hi","Nice to meet you")

# checkbox (agreeing terms and conditions)
if st.checkbox("Do you agree with our terms and conditions", help="You must agree to proceed"):
    st.write("Thanks for agreeing")

# color pick
color = st.color_picker("Select color")
st.write("You selected",color)

# rating
languages = st.text_input("Enter languages you know (Comma separated)", value='Bengali')
languages = [i.strip() for i in languages.split(",")]
st.subheader("How do you rate your languages")
for lang in languages:
    st.write(lang)
    st.slider(lang, min_value=0.0, max_value=10.0, step=1.0)

# submit button
st.button("Submit your response")