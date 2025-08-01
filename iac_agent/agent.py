# agent.py

from smolagents import LiteLLMModel, CodeAgent
from tools.validate_yaml import ValidateYAMLTool
from tools.yaml_parser import YamlParserTool
from dotenv import load_dotenv
import yaml
from smolagents.tools import Tool

# from .smart_code_agent import SmartCodeAgent
import os

# load .env file (i.e., openai api key)
load_dotenv()

# Initialize the LLM model using your OpenAI key
model = LiteLLMModel(
    model_id = "openai/gpt-3.5-turbo",
    api_key = os.getenv("OPENAI_API_KEY")
)

yaml_parser_tool = YamlParserTool()

# Create the agent from CodeAgent
agent = CodeAgent(
    model = model,
    max_steps = 4,
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
    runbook = agent.run(task)
    # print("++++++++++ Final Agent Response (runbook):\n", response)
    return runbook

