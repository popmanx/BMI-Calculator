import streamlit as st
st.title("BMI Calculator App")

weight = st.number_input("What is your weight(KG)")
hight = st.number_input("What is your hight(Meters)")



st.camera_input("smaile")
def bmi_calc(weight,hight):
    bmi = round(weight / (hight ** 2),1)
    if bmi > 29.9:
        rating = 'are at risk of being obese, take care'
    elif 24.9 < bmi < 30:
        rating = 'are at risk of being overweight, takr care'
    elif 18.4 < bmi < 25:
        rating = 'are normal, well done'
    else:
        rating = 'are at risk of being underweight, take care'
    return f"your BMI is {bmi} and you {rating} "

if st.button("calculate BMI"): 
    st.balloons()
    st.write(bmi_calc(weight,hight))