# 🧠 Autonomous Research Agent (Multi-Agent GenAI System)

An end-to-end Autonomous Research Agent that generates structured, high-quality reports from a user-provided topic using a multi-agent architecture built with LangGraph and LLMs.

## Features

- Generate full research reports from a single topic
- Multi-agent pipeline (Planner → Researcher → Writer → Synthesizer)
- Section-wise structured report generation
- Clean and consistent output formatting
- Optimized to handle LLM rate limits and token constraints
- Interactive UI using Streamlit

## Architecture

User Input (Topic)  
↓  
Planner Agent  
↓  
Researcher Agent  
↓  
Writer Agent (per section)  
↓  
Synthesizer  
↓  
Final Report  

## Agents Overview

### Planner Agent
Breaks the input topic into structured sections and ensures logical, non-overlapping coverage.

### Researcher Agent
Generates concise and relevant research points, filtering noise and focusing on key insights.

### Writer Agent
Converts research into well-written sections with clarity, coherence, and a professional tone.

### Synthesizer
Combines all sections into a final report and generates a clean, formatted output.

## Tech Stack

- LangGraph (multi-agent orchestration)
- LangChain (prompt & chain management)
- Groq LLM (fast inference)
- Pydantic (structured outputs)
- Streamlit (UI)
- Python

## Project Structure

.
├── agents.py          # Agent logic  
├── helper.py          # Prompts & LLM chains  
├── graph.py           # Workflow definition  
├── app.py             # Streamlit UI  
├── config.py          # Model config  
├── .env               # API keys  
└── README.md  

## Setup & Installation

```bash
git clone https://github.com/your-username/autonomous-research-agent.git
cd autonomous-research-agent

python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows

pip install -r requirements.txt
```
🔑 Environment Variables

Create a .env file and add your API key:
```bash
GROQ_API_KEY=your_api_key
```
▶️ Run the App
```bash
streamlit run app.py
```
## Author

Abhirup
