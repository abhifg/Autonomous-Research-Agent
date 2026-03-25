import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from graph import graph

st.title("Autonomous Research Agent")

topic=st.text_area("Enter your topic")
generate=st.button("Generate")

if generate and topic:
    with st.spinner("Generating report... please wait ⏳"):
        response=graph.invoke({"topic":topic})["final_report"]
    st.markdown(response)
if generate and topic=="":
    st.error("Please enter your topic")







