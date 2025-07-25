import streamlit as st
import os
from src.langgraph.UI.uiconfig import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_control = {}

    def loadui(self):
        st.set_page_config(page_title= f"Oh yeah! {self.config.get_page_title()}",layout="wide")
        st.header(f"Oh yeah baby someone seeing me")

        with st.sidebar:
            llm_options= self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()


            ## boxes
            self.user_control['selected_LLM'] = st.selectbox("select LLM",llm_options)

            if self.user_control['selected_LLM'] == 'Groq':
                model_options = self.config.get_groq_model_options()
                self.user_control['selected_groq_model'] = st.selectbox("selected_model",model_options)
                self.user_control["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("Enter API Key",type = "password")
            

            self.user_control["selected usecases"] = st.selectbox("select Usecase",usecase_options)

        return self.user_control