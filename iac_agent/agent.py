# agent.py

from smolagents import LiteLLMModel, CodeAgent
from tools.validate_yaml import ValidateYAMLTool
from dotenv import load_dotenv
import os

# load .env file (i.e., openai api key)
load_dotenv()

# Initialize the LLM model using your OpenAI key
model = LiteLLMModel(
    model_id = "openai/gpt-3.5-turbo",
    api_key = os.getenv("OPENAI_API_KEY")
)

# Create the agent
agent = CodeAgent(
    model = model,
    max_steps = 5,
    tools = [ ValidateYAMLTool()]
)

# Core function to generate a playbook from a high-level admin task
def generate_ansible_playbook(task: str) -> str:
    response = agent.run(task)
    return response

