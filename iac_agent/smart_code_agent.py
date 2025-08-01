from smolagents import CodeAgent
import traceback

class SmartCodeAgent(CodeAgent):
    def is_yaml(self, code: str) -> bool:
        try:
            if code.strip().startswith("```"):
                code = code.split("```")[1]
            import yaml
            yaml.safe_load(code)
            return True
        except Exception:
            return False

    def parse_code_blocks(self, text: str):
        print("++++++++++++++ I AM OVERRIDING parse_code_blocks +++++++++++")
        if "```yaml" in text:
            print("++++++++++++++ I AM YAML!! +++++++++++")
            return [text.split("```yaml")[1].split("```")[0].strip()]
        return super().parse_code_blocks(text)

    def run(self, task: str) -> str:
        print("++++++++++++++ I AM OVERRIDING run() +++++++++++")

        self.memory.history = []  # reset conversation
        messages = [{"role": "user", "content": task}]

        for step in range(self.max_steps):
            print(f"\n===== REASONING STEP {step + 1} =====")

            # ✅ Correct: use self.think()
            thought = self.think(messages)
            print(f"Model Response:\n{thought}")

            # ✅ Handle YAML-aware parsing
            code_blocks = self.parse_code_blocks(thought)
            print("Extracted code blocks:", code_blocks)

            if not code_blocks:
                print("No code blocks found. Returning full response.")
                return thought

            for code in code_blocks:
                result = self.execute_code_block(code)
                print(f"Execution Result:\n{result}")
                messages.append({"role": "assistant", "content": thought})
                messages.append({"role": "user", "content": result})

        return self.extract_final_answer(messages)
