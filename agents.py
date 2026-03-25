import os
from dotenv import load_dotenv
load_dotenv()
from typing_extensions import TypedDict,Annotated,List
from langgraph.types import Send
import operator
import time
from helper import Section,planner_chain,researcher_chain,writer_chain,llm

class State(TypedDict):
    topic: str
    sections: List[Section]
    research_data: str
    completed_sections: Annotated[List[str], operator.add]
    final_report: str


class WorkerState(TypedDict):
    topic:str
    section: Section
    research_data: str
    completed_sections: Annotated[List[str], operator.add]

def orchestrator(state: State):
    response = planner_chain.invoke({
        "topic": state["topic"]
    })
    return {"sections": response.sections}

def researcher(state: State):
    response = researcher_chain.invoke({
        "topic": state["topic"],
        "sections": state["sections"]
    })
    time.sleep(2)
    return {"research_data": response}

def worker(state:WorkerState):
    written=writer_chain.invoke(
        {
            "topic":state["topic"],
            "section":state["section"].name,
            "research_content":state["research_data"]
        }
    )
    time.sleep(1.5)
    return {"completed_sections":[written]}

def assign_worker(state:State):
    return [Send("Writer + Editor",{"topic":state["topic"],"section":s,"research_data":state["research_data"]}) for s in state["sections"]]

def synthesizer(state:State):
    completed_sections=state["completed_sections"]
    report_body = "\n\n---\n\n".join(completed_sections)
    title = llm.invoke(f"""
        Generate ONE concise professional report title.

        Topic: {state['topic']}

        Rules:
        - Return ONLY one title
        - No explanations
        """
    ).content.strip().strip('"')
    final_report=f"# {title}\n\n{report_body}"
    return {"final_report":final_report}
