import streamlit as st

st.title("Unit Converter")

factor = {'mm' : 1, 'cm' : 0.1, 'm' : 0.001, 'km' : 0.000001}

with st.container(border=True):
    st.write("")

    inputnum, baseunit, targetunit, result = st.columns(4)
    with inputnum:
        input_value = st.number_input("Enter Number")
    with baseunit:
        base_unit = st.radio("Base Unit",options = factor.keys())
    with targetunit:
        target_unit = st.radio("Target Unit",options = factor.keys())
    with result:
        st.write("Result")

        base_factor = factor[base_unit]
        target_factor = factor[target_unit]

        st.write(base_unit, base_factor)
        st.write(target_unit, target_factor)

        result = (input_value / base_factor) * target_factor
        st.latex(f"{result}{target_unit}")

with st.container():
    st.latex(r"\text{result}  =  \frac{\text{input value}}{\text{base factor}} \times \text{target factor}")
