import streamlit as st
from src.langgraph.UI.streamlit.loadui import LoadStreamlitUI
from src.langgraph.llms.groqllm import GroqLLM
from src.langgraph.graph.graph_builder import GraphBuilder
from src.langgraph.UI.streamlit.display_result import DisplayResultStreamlit

def load_langgraph_app():


    ui = LoadStreamlitUI()
    user_input = ui.loadui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return
    
    user_message = st.chat_input("Enter your message:")

    if user_message: 
        try:
            obj_llm = GroqLLM(user_control_input=user_input)
            model = obj_llm.get_llm_model()
            if not model:
                st.error("LLM model could not be initialized")
            usecase = user_input.get('selected usecases')
            graph_builder = GraphBuilder(model=model)
            try:
                graph = graph_builder.setup(usecase)
                DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()

            except Exception as e:
                st.error(f"Error in the initialization of the graph = {e}")

        except Exception as e:
            st.error(f"User input error : {e}")
            return

