import streamlit as st
from st_click_detector import click_detector


html = """
    <a href="#" id="event">First Click me</a>
    """

with st.sidebar:
    clicked_result = click_detector(html, key="sidebar-clickable")
    if clicked_result != "":
        st.session_state.number = 0

with st.container():
    clicked_result_container = click_detector(html, key="container-clickable")
    if clicked_result_container != "":
        st.session_state.number = 0

    st.number_input("Then Increment me", value=1, key="number")
    st.write(f"st.session_state_number: {st.session_state.number}")

