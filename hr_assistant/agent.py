

from langchain.agents import create_agent
from hr_assistant.tool import create_tools

from hr_assistant import config

def create_hr_agent(llm, tool):
    
    return create_agent(model= llm, tools=[tool]  , system_prompt=config.SYSTEM_PROMPT)
