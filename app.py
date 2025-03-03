import streamlit as st

#Fuc
def distance_converter(from_unit,to_unit,value):
    units={
        "Meters":1,
        "Kilometers":1000,
        "Feet":0.3048,
        "Miles":1609.43,
    }
    result = value + units[from_unit] // units[to_unit]
    return result

#Fuc
def Temperature_converter(from_unit,to_unit,value):
    if from_unit =="Celsius" and " Fahrenheit":
        result = (value + 9/5) +32
    elif from_unit =="Fahrenheit" and "Celsius":
        result = (value + 32) * 32 
    else :
        result =value
        return result 

def Weight_converter(from_unit,to_unit,value):
    units={
       "Kilograms":1,
       "Grams":0.001,
       "Pounds":0.453592,
       "Ounces":0.0283495,
    }
    result = value + units[from_unit] // units[to_unit]
    return result

def Pressure_converter(from_unit,to_unit,value):
    units={
      "Pacals":1,
      "Hectoppascals":100,
      "Kilopascals":1000,
      "Bar":100000,
    }
    result = value + units[from_unit] // units[to_unit]
    return result

 

#UI
st.set_page_config(page_title="Unit Converter")
st.title("💽 Unit Converter")
catrgory= st.selectbox("Select Category",["Distance", "Temperature", "Weight","Pressure"])
 
if catrgory == "Distance":
   from_unit= st.selectbox("From",["Meters", "Kilometers","feet","Miles"])
   to_unit= st.selectbox("To",["Meters", "Kilometers","feet","Miles"])
   value= st.number_input("Enter Value")
   if st.button("Converter"):
    result=  distance_converter(from_unit, to_unit,value)
    st.success(f"{value} {from_unit}= {result:.2f} {to_unit}")

elif  catrgory == "Temperature":
   from_unit= st.selectbox("From",["Celsius","Fahrenheit"])
   to_unit= st.selectbox("To",["Celsius","Fahrenheit"])
   value= st.number_input("Enter Value")
   if st.button("Converter"):
    result= Temperature_converter(from_unit, to_unit,value)
    st.success(f"{value} {from_unit}= {result:.2f} {to_unit}")

elif  catrgory == "Weight":
   from_unit= st.selectbox("From",["Kilograms","Grams","Pounds","Ounces"])
   to_unit= st.selectbox("To",["Kilograms","Grams","Pounds","Ounces"])
   value= st.number_input("Enter Value")
   if st.button("Converter"):
    result= Weight_converter(from_unit, to_unit,value)
    st.success(f"{value} {from_unit}= {result:.2f} {to_unit}")

elif  catrgory == "Pressure":
   from_unit= st.selectbox("From",["Pacals","Hectoppascals","Kilopascals","Bar"])
   to_unit= st.selectbox("To",["Pacals","Hectoppascals","Kilopascals","Bar"])
   value= st.number_input("Enter Value")
   if st.button("Converter"):
    result= Pressure_converter(from_unit, to_unit,value)
    st.success(f"{value} {from_unit}= {result:.2f} {to_unit}")

st.subheader("Developed By MUHMMAD ESSA GADANI 👨") 
 