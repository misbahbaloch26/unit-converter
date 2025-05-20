import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="🔄")

st.title("🔄 Simple Unit Converter")
st.markdown("Convert between different units of **Length**, **Weight**, and **Temperature**.")

conversion_type = st.selectbox("Choose conversion type", ["Length", "Weight", "Temperature"])

if conversion_type == "Length":
    units = {
        "Meter": 1,
        "Kilometer": 1000,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Foot": 0.3048,
        "Inch": 0.0254,
        "Mile": 1609.34,
        "Yard": 0.9144
    }

elif conversion_type == "Weight":
    units = {
        "Kilogram": 1,
        "Gram": 0.001,
        "Milligram": 0.000001,
        "Pound": 0.453592,
        "Ounce": 0.0283495
    }

elif conversion_type == "Temperature":
    temp_units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From", temp_units)
    to_unit = st.selectbox("To", temp_units)
    value = st.number_input("Enter value")

    def convert_temperature(val, from_u, to_u):
        if from_u == to_u:
            return val
        elif from_u == "Celsius":
            if to_u == "Fahrenheit":
                return val * 9/5 + 32
            elif to_u == "Kelvin":
                return val + 273.15
        elif from_u == "Fahrenheit":
            if to_u == "Celsius":
                return (val - 32) * 5/9
            elif to_u == "Kelvin":
                return (val - 32) * 5/9 + 273.15
        elif from_u == "Kelvin":
            if to_u == "Celsius":
                return val - 273.15
            elif to_u == "Fahrenheit":
                return (val - 273.15) * 9/5 + 32

    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {round(result, 2)} {to_unit}")

    st.stop()  

from_unit = st.selectbox("From Unit", list(units.keys()))
to_unit = st.selectbox("To Unit", list(units.keys()))
value = st.number_input("Enter value", format="%f")

if st.button("Convert"):
    base_value = value * units[from_unit]
    result = base_value / units[to_unit]
    st.success(f"{value} {from_unit} = {round(result, 4)} {to_unit}")
