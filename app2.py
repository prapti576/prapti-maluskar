import streamlit as st

st.title("Simple Calculator App")

num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

operation = st.selectbox(
    "Choose operation",
    ["add", "sub", "multiply", "div"]
)


if st.button("Calculate"):
    if operation == "add":
        result = num1 + num2
    elif operation == "sub":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "div":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"

    st.success(f"Result: {result}")