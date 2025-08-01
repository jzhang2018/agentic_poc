# tools/yaml_parser.py

import yaml
from smolagents.tools import Tool

class YamlParserTool(Tool):
    
    print("++++++++++++++ I AM YamlParserTool ++++++++++++++")
    name = "parse_yaml"
    description = "Parses a YAML string into a Python dictionary."
    inputs = {
        "yaml_str": {"type": "string", "description": "YAML formatted string"}
    }
    output_type = "object"

    def forward(self, yaml_str: str) -> dict:
        print("🔥🔥 YamlParserTool was called 🔥🔥")
        try:
            return yaml.safe_load(yaml_str)
        except yaml.YAMLError as e:
            return {"error": str(e)}
