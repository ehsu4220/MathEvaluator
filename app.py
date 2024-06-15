'''
Primary file for the streamlit frontend
'''
import streamlit as st
from Evaluator import Evaluator

# Initialize Evaluator
evaluator = Evaluator()

# Title
st.title("Expression Evaluator")

# Input Field
expression = st.text_input("Enter an expression to evaluate:")

variables = {}

# Button to evaluate the expression
if st.button("Evaluate"):
    try:
        # Parse and evaluate the expression
        result_function = evaluator.parse(expression, variables)
        result = result_function
        st.write(f"Result: {result}")
    except Exception as e:
        st.write(f"Error: {e}")
