# smart_code_agent.py

import yaml
from smolagents import CodeAgent

class SmartCodeAgent(CodeAgent):
    def is_yaml(self, code: str) -> bool:
        try:
            # Remove Markdown-style wrapping if present
            if code.strip().startswith("```"):
                code = code.split("```")[1]
            yaml.safe_load(code)  # if the code is yaml or not
            return True
        except Exception:
            return False
    
    def run(self, task: str) -> str:
        messages = [{"role": "user", "content": task}]
       
        reply = self.model(messages)

        if hasattr(reply, 'content'):
            # unwrap if ChatMessage-like object
            reply_text = reply.content
        
        elif isinstance(reply, dict):
            reply_text = reply['choices'][0]['message']['content']
        
        else:
            reply_text = str(reply)
        
        print(reply_text)

        if self.is_yaml(reply_text):
            print("SmartCodeAgent detected YAML - skipping execution.")
            return reply_text

        return super().run(task)
