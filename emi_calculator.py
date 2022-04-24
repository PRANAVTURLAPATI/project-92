import streamlit as st
def calculate_emi(p, n, r):
    return round(p * r/100 * (((1 + r/100)**n)/((1+r/100)**n - 1)), 3)
def calculate_outstanding_balance(p, n, r, m):
    return round((p*(1+r/100)**n - (1+r/100)**m)/((1+r/100)**n - 1) , 3)
st.subheader("EMI Calculator")
principal = st.number_input("Principal Amount", 1000.00, 1000000.00, step = 0.01)
tenure = st.number_input("Tenure", 1, 30)
rate_of_interest = st.number_input("Rate of Interest", 1.00, 15.00, step = 0.01)
months = st.number_input("Months", step = 1)
if st.button("Calculate EMI"):
    st.write(calculate_emi(principal, 12 * tenure, rate_of_interest / 12))
if st.button("Calculate Outstanding Loan Balance"):
    st.write(calculate_outstanding_balance(principal,12 * tenure, rate_of_interest / 12, months))