from langgraph.graph import StateGraph,START,END
from agents import orchestrator,researcher,worker,assign_worker,synthesizer,State

workflow=StateGraph(State)

workflow.add_node("Orchestrator",orchestrator)
workflow.add_node("Researcher",researcher)
workflow.add_node("Writer + Editor",worker)
workflow.add_node("Synthesizer",synthesizer)

workflow.add_edge(START,"Orchestrator")
workflow.add_edge("Orchestrator","Researcher")
workflow.add_conditional_edges("Researcher",assign_worker,["Writer + Editor"])
workflow.add_edge("Writer + Editor","Synthesizer")
workflow.add_edge("Synthesizer",END)

graph=workflow.compile()


