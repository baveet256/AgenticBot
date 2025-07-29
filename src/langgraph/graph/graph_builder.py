
from langgraph.graph import StateGraph,START,END
from src.langgraph.state.state import State

from src.langgraph.nodes.chatbot_node import BasicChatbot


class GraphBuilder:
    def __init__(self,model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def chatbot_node_build(self):
        self.chatbot_maker = BasicChatbot(self.llm)

        self.graph_builder.add_node("chatbot",self.chatbot_maker.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def setup(self,usecase:str):
        if usecase == "Basic Chatbot":
            self.chatbot_node_build()

        return self.graph_builder.compile()