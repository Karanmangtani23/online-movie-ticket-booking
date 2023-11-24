import streamlit as st
import database as db

def execute():
    commandline = st.text_input("Enter to execute: ")
    if st.button("Execute Query"):
        res = db.execute_queries(commandline)
        st.success("Successfully Executed Queries")
        if res:
            with st.expander("View Details"):
                st.dataframe(res)