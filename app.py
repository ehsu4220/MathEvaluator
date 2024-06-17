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

# Initialize variables dictionary
if "variables" not in st.session_state:
    st.session_state["variables"] = {}

# Function to add a variable
def add_variable(name, value):
    st.session_state["variables"][name] = value

# Function to clear variables
def clear_variables():
    st.session_state["variables"].clear()

# Evaluator page
if page == "Evaluator":
    st.title("Expression Evaluator")
    
    st.write("")
    st.write("")
    
    # Input Field
    exp_col_1, exp_col_2, exp_col_3 = st.columns([0.4, 1, 0.3])
    with exp_col_1:
        st.write("")
        st.subheader("Expression:")
    with exp_col_2:
        expression = st.text_input("Enter an expression to evaluate:")
    with exp_col_3:
        st.write("")
        st.write("")
        # Button to evaluate the expression
        if st.button("Evaluate"):
            try:
                # Parse and evaluate the expression
                result = evaluator.parse(expression, st.session_state["variables"])
                st.subheader(f"= {result}")
            except Exception as e:
                st.write(f"Error: {e}")
    
    # Display current variables
    st.write("")
    st.write("")
    var_col1, var_col2, var_col3, var_col4 = st.columns([0.55, 0.4, 1, 0.4])
    with var_col1:
        st.write("")
        st.subheader("Variables:")
    with var_col2:
        add_var_name = st.text_input("Variable Character", key="add_var_name")
    with var_col3:
        add_var_value = st.number_input("Variable Value", key="add_var_value")
    with var_col4:
        st.write("")
        st.write("")
        if st.button("Add", key="add_button"):
            add_variable(add_var_name, add_var_value)
    
    st.write("")
    # Clear and Display
    display_col_1, display_col_2 = st.columns([0.3, 1])      
    with display_col_1:
        if st.button("CLEAR"):
            clear_variables()  
    with display_col_2:
        if len(st.session_state["variables"]) == 0:
            st.write("No variables defined!")
        else:
            for var_name, var_value in st.session_state["variables"].items():
                st.write(f"- **{var_name}** = `{var_value}`")
                

elif page == "Documentation":
    st.title("Documentation")
    
    st.markdown("""
        
        This project provides a simple expression evaluator implemented in Python. 
        
        Code is derived off of the Java implementation provided by Boann: https://stackoverflow.com/questions/3422673/how-to-evaluate-a-math-expression-given-in-string-form
        
        ## Usage of Web UI
        1. **Input an expression**: Enter the expression you want to evaluate.
        2. **Evaluate**: Click the "Evaluate" button to get the result.
        
        ## Functions supported
        - `sqrt(x)`
            - Square root of `x`
            
        - `sin(x)`
            - Sine of `x`, `x` as degrees, returned as radians
            
        - `cos(x)`
            - Cosine of `x`, `x` as degrees, returned as radians
            
        - `tan(x)`
            - Tangent of `x`, `x` as degrees, returned as radians
            
        - `sqr(x)`
            - `x` squared
            
        - `exp(x)`
            - raises `e` to the power of `x`
            
        - `ln(x)`
            - Log base `e` of `x`
        
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
        variables = {'x' : 1}

        # Result
        result = evaluator.parse(expression, variables)
        print(result) # Expected 9.34
        ```
        
        ## Other Notes:
        - Any variable not defined will be replaced with `0`
        - Any variable declared as `e` will be defined as `math.e`
    """)

elif page == "About":
    st.title("About")
    
    
    st.markdown("""
        ## Github
        https://github.com/ehsu4220/MathEvaluator
        
        ## Linkedin
        https://www.linkedin.com/in/eric-hsu-234718126/
    """)
