import streamlit as st
from src.langgraph.UI.streamlit.loadui import LoadStreamlitUI



def load_langgraph_app():


    ui = LoadStreamlitUI()
    user_input = ui.loadui()

    user_message = st.chat_input("Enter your message:")

