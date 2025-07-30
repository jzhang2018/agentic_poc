# tools/validate_yaml.py

import yaml
from smolagents.tools import BaseTool

class ValidateYAMLTool(BaseTool):
    name = "validate_yaml"
    description = "Validate if the input string is a valid Ansible playbook in YAML format"

    def __call__(self, input: str) -> str:
        try:
            data = yaml.safe_load(input)
            if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                return "YAML is valid"
            else:
                return "YAML is loaded but doesn't look like a valid playbook list"
        except yaml.YAMLError as e:
            return f"YAML parsing error: {str(e)}"

    def to_code_prompt(self) -> str:
        return (
            "This tool validates whether the input string is a valid Ansible playbook "
            "written in YAML format. It returns 'YAML is valid' if valid, or an error "
            "message if invalid."
        )