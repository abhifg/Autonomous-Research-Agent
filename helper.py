import os
from dotenv import load_dotenv
load_dotenv()
from pydantic import BaseModel,Field
from typing import Annotated,Literal
from typing_extensions import List
from langchain_groq import ChatGroq
import operator
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config import LLM_MODEL

class Section(BaseModel):
    name:str=Field(description="name of the section")
    description:str=Field(description="Overview of the section")

class Sections(BaseModel):
    sections:List[Section]=Field(description="Different sections of the report")

llm=ChatGroq(model=LLM_MODEL,temperature=0)

planner=llm.with_structured_output(Sections)

planner_prompt=""" You are a planning agent for an autonomous research system.

Your task is to break down a given research topic into clear, logical, 
and well-structured sections for a detailed report.

Guidelines:
- Create 5-7 sections
-- Description should be a single short sentence (max 15 words)
- Ensure sections are specific and meaningful (avoid generic titles like "Introduction" or "Conclusion")
- Cover different aspects of the topic (e.g., overview, applications, challenges, trends, etc.)
- Avoid overlapping or redundant sections
- Make the structure suitable for a professional report
"""
planner_template=ChatPromptTemplate.from_messages(
    [
        ("system",planner_prompt),
        ("human","Here is topic provided by user {topic}")
    ]
)
planner_chain=planner_template|planner


researcher_prompt=""" You are a research agent.

Your task is to gather relevant, factual, and concise information 
for a given research topic by user and its sections provided by planner.

Instructions:
- Write a suitable title for the report
- Use the provided topic and sections to extract useful information
- Focus only on relevant and high-quality content
- Remove ads, irrelevant text, and noise
- Summarize key points clearly
- Preserve important facts, numbers, and insights
- Do NOT hallucinate or add information not present in the data

Note - Keep it more short and crisp just main points.
Output format:
Return structured notes grouped by section:

Section: <section name>
- key point 1
- key point 2
- key point 3

Include source references if available.
"""
researcher_template=ChatPromptTemplate.from_messages(
    [
        ("system",researcher_prompt),
        ("human","Here is the Topic : {topic}\n and Sections : {sections} of the report")
    ]
)
researcher_chain=researcher_template|llm|StrOutputParser()

writer_prompt=""" You are a professional writer and editor.

Your task is to write ONE section of a report.

Instructions:
- Write ONLY for the given section
- Use the provided research content
- Do NOT hallucinate
- Keep it clear, structured, and professional
- use tables with new data (don't use same data already written)

Output format (STRICT):

{section} (in bold format)

<Write 80–120 words>

Rules:
- Do NOT generate multiple sections
- Do NOT add extra commentary
- Do NOT include phrases like "Here is..." or "Refined version"
- Return ONLY the section
"""

writer_template=ChatPromptTemplate.from_messages(
    [
        ("system",writer_prompt),
        ("human","Here is the following information : Topic: {topic}\n Section : {section}\n and Research Content : {research_content}")
    ]
)

writer_chain=writer_template|llm|StrOutputParser()









