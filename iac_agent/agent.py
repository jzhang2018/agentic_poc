# agent.py

from smolagents import LiteLLMModel, CodeAgent
from tools.validate_yaml import ValidateYAMLTool
from dotenv import load_dotenv
from .smart_code_agent import SmartCodeAgent
import os

# load .env file (i.e., openai api key)
load_dotenv()

# Initialize the LLM model using your OpenAI key
model = LiteLLMModel(
    model_id = "openai/gpt-3.5-turbo",
    api_key = os.getenv("OPENAI_API_KEY")
)

# Create the agent from SmartCodeAgent
agent = SmartCodeAgent(
    model = model,
    max_steps = 3,
    tools = [ ValidateYAMLTool()]   # dynamically used during reasoning 
)

# Core function to generate a playbook from a high-level admin task
def generate_ansible_playbook(task: str) -> str:
    response = agent.run(task)
    return response

