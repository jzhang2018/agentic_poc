# agent.py

from smolagents import LiteLLMModel, CodeAgent
from tools.yaml_parser import YamlParserTool
from dotenv import load_dotenv
import yaml, os
from smolagents.tools import Tool

# load .env file (i.e., openai api key)
load_dotenv()

# Initialize the LLM model
model = LiteLLMModel(
    model_id = "openai/gpt-3.5-turbo",
    api_key = os.getenv("OPENAI_API_KEY")
)

# yaml parser tool for agent toolbox
yaml_parser_tool = YamlParserTool()

# Create an agent from CodeAgent
agent = CodeAgent(
    model = model,
    max_steps = 5,
    tools = [yaml_parser_tool]
)

# Core function to generate a runbook
def generate_runbook(task: str) -> str:  
    # What happens in agent.run(task)?
    # - agent talks to the LLM
    # - agent parses the return content (assuming it is Python!)
    # - agent iterates reasoning steps (up to max_steps)
    # - agent returns a final response. It could be valid code string, or partial/imcomplete code 
    #       or nothing/invalid code
    # - agent does not throw an exception if the there is a failure 
    return agent.run(task)

