import streamlit as st

st.title("Welcome to my hard earned website")
st.header("Python")
st.subheader("Java")
st.markdown("I love python")
st.code("""for i in range(1,5,1):
                print("Hello")
        """)

import pandas as pd

dataset1 = pd.read_csv("EXCEL_PRACTICE_20_MARCH_2025.csv")

st.dataframe(dataset1)

name = st.text_input("Enter your name")
fname = st.text_input("Enter your Father's name")
adr = st.text_input("Enter your Text: ")
classdata = st.selectbox("Enter your Class :",(1,2,3,4,5,6))

button = st.button("Done")
if button :
    st.markdown(f"""
    Name: {name}
    Father Name : {fname}
    address : {adr}
    class : {classdata}
""")


import streamlit as st

st.title('BMI Calculator')

weight = st.number_input("Enter your weight (in kgs)")
status = st.radio('Select your height format:', ('cms', 'meters', 'feet'))

if status == 'cms':
    height = st.number_input('Centimeters')
    bmi = weight / ((height / 100) ** 2)
elif status == 'meters':
    height = st.number_input('Meters')
    bmi = weight / (height ** 2)
else:
    height = st.number_input('Feet')
    bmi = weight / ((height / 3.28) ** 2)

if st.button('Calculate BMI'):
    st.text(f"Your BMI Index is {bmi:.2f}")
if bmi < 16:
    st.error("You are Extremely Underweight")
elif bmi < 18.5:
    st.warning("You are Underweight")
elif bmi < 25:
    st.success("Healthy")
elif bmi < 30:
    st.warning("Overweight")
else:
    st.error("Extremely Overweight")
