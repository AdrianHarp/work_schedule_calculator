import streamlit as st
from logic import status
st.title("art thou working :O")


date = st.date_input("input target date")
mandatory_one = st.date_input("input first mandatory date",key="man1")
mandatory_two = st.date_input("input second mandatory date",key="man2")
if date and mandatory_one and mandatory_two:
    try:
        date_str = date.strftime("%Y-%m-%d")
        mandatory_one_str = mandatory_one.strftime("%Y-%m-%d")
        mandatory_two_str = mandatory_two.strftime("%Y-%m-%d")

        result = status(date_str, mandatory_one_str, mandatory_two_str)
        st.write(result)
    except Exception as e:
        st.error(f"Something went wrong: {e}")
else:
    st.write("Waiting for input")








