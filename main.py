import streamlit as st



st.title("Calculator")

st.subheader("Simple Calculator")

def calculator():
    col1, col2 = st.columns(2)
    
    
    with col1:
        num1 = st.number_input("Enter Your First Number", value=0.0)
        
    with col2:
        num2 = st.number_input("Enter Your Second Number", value=0.0)
    
    operator = st.selectbox("Choose An Operator", ["Addition (+)", "Substraction (-)", "Multiplication (*)", "Division (/)"])
    
    if st.button("Calculate"):
        try:
            if operator == "Addition (+)":
                result = num1 + num2
                symbol = "+"
            elif operator == "Substraction (-)":
                result = num1 - num2
                symbol = "-"
            elif operator == "Multiplication (*)":
                result == num1 * num2
                symbol = "*"
            else:
                if num2 == 0:
                    st.error("Error: Division by Zero!")
                    return
                result = num1 / num2
                symbol = "/"
            st.success(f"{num1} {symbol} {num2} = {result}")
        except Exception as e:
            st.error(f"An Error Occured: {str(e)}")

if __name__ =="__main__":
    calculator()