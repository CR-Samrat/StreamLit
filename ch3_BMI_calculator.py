import streamlit as st

def bmi_calc():
    st.header("BMI Calculator")
    with st.form("BMI Calculator", clear_on_submit=False):
        col1, col2, col3 = st.columns([3,2,1])
        with col1:
            weight = st.number_input("Enter your weight in KG",min_value=0.0,max_value=200.0)
        with col2:
            height = st.number_input("Enter your height in meters",min_value=0.0,max_value=10.0)
        with col3:
            submit = st.form_submit_button(label = "Calculate")

    if submit:
        bmi = round((weight/(height**2)),2)
        if bmi <= 18.5:
            st.warning("Underweight")
        elif bmi > 18.5 and bmi <= 24.9:
            st.success("Healthy")
        elif bmi > 24.9 and bmi < 29.9:
            st.warning("Overweight")
        else:
            st.error("OBESE")

def feet_to_meter_calc():
    st.title("Feet to Meter Converter")

    with st.form("Feet to Meter Converter", clear_on_submit=False):
        col1, col2 = st.columns([2, 2])
        with col1:
            height_feet = st.number_input("Enter height in feet", min_value=0.0, max_value=10.0, value=0.0, step=0.1)
        with col2:
            height_meter = round((height_feet * 0.3048),2)
            st.write("Height in meters")
            st.success(height_meter)
        submit = st.form_submit_button(label="Convert")

    if submit:
        st.write("Conversion completed!")

ch = st.sidebar.selectbox("Services", ["BMI Calculator","Feet to Meter Converter"])
if ch == "BMI Calculator":
    bmi_calc()
else:
    feet_to_meter_calc()