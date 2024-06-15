'''
Primary file for the streamlit frontend
'''
import streamlit as st
from Evaluator import Evaluator

# Initialize Evaluator
evaluator = Evaluator()

# Initial Start
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Evaluator", "Documentation", "About"])

variables = {'x' : 1}

# Evaluator page
if page == "Evaluator":
    st.title("Expression Evaluator")
    
    # Input Field
    st.subheader("Expression")
    expression = st.text_input("Enter an expression to evaluate:")

    # Display current variables
    st.subheader("Variables")
    for var_name, var_value in variables.items():
        st.write(f"- {var_name}: {var_value}")
        
    # Button to evaluate the expression
    if st.button("Evaluate"):
        try:
            # Parse and evaluate the expression
            result = evaluator.parse(expression, variables)
            st.write(f"Result: {result}")
        except Exception as e:
            st.write(f"Error: {e}")

elif page == "Documentation":
    st.title("Documentation")
    
    st.markdown("""
        
        This project provides a simple expression evaluator implemented in Python. 
        
        ## Usage of Web UI
        1. **Input an expression**: Enter the expression you want to evaluate.
        2. **Evaluate**: Click the "Evaluate" button to get the result.
        
        ## Functions supported
        - `sqrt(x)`
            - Square root of `x`
            
        - `sin(x)`
            - Sine of `x`, `x` converted to radians
            
        - `cos(x)`
            - Cosine of `x`, `x` converted to radians
            
        - `tan(x)`
            - Tangent of `x`, `x` converted to radians
            
        - `sqr(x)`
            - `x` squared
            
        - `exp(x)`
            - raises `e` to the power of `x`
            
        - `log(x)`
            - Log base `e` of x
        
        - `log10(x)`
            - Log base 10 of `x`
            
        - `abs(x)`
            - Absolute value of `x`

        - `neg(x)`
            -  Negation of `x`
            
        - `round(x, decimal_places)`
            - Rounds `x` to the number of decimal places
            - **NOTE**: May have unexpected behavior. Look into **Decimal Value Binary Representation**
        
        
        ## Example
        
        Below is an example code snippet that shows how to use the evaluator class:
        ```python
        from Evaluator import Evaluator

        # Initialize the Evaluator
        evaluator = Evaluator()

        # Expression
        expression = "round(3 + 5 * x^2 + 1.337, 2)"

        # A dictionary to hold variables if needed (currently empty)
        variables = {x : 1}

        # Result
        result = evaluator.parse(expression, variables)
        print(result) # Expected 9.34
        ```
    """)

elif page == "About":
    st.title("About")
    
    
    st.markdown("""
        ## Github
        https://github.com/ehsu4220/MathEvaluator
        
        ## Linkedin
        https://www.linkedin.com/in/eric-hsu-234718126/
    """)
