# states
from agent.models.states.state import State, InputState

# langgraph libraries
from langgraph.graph import StateGraph, START, END

# Import nodes
from agent.nodes.lower_case import lower_case
from agent.nodes.generate_response import generate_response

workflow = StateGraph(
    state_schema=State,
    input=InputState
)

# Nodes
# lower_case node
workflow.add_node("lower_case", lower_case)
# generate_response
workflow.add_node("generate_response", generate_response)

# connect Edges
workflow.add_edge(START, "lower_case")
workflow.add_edge("lower_case", "generate_response")
workflow.add_edge("generate_response", END)

# compile graph
graph = workflow.compile()

# export graph
with open("./graph.png", "wb") as file:
    file.write(graph.get_graph().draw_mermaid_png())




