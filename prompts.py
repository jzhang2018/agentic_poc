# prompts.py

PROMPT_TEMPLATES = {
    "ansible": """You are generating an Ansible YAML playbook.
                  Requirements:
                  - Use native Ansible modules when possible.
                  - Use fully qualified collection names (e.g., ansible.builtin.shell).
                  - Use check_mode: false for all ansible.builtin.shell or ansible.builtin.command tasks.
                  - When use ansible.builtin.shell or ansible.builtin.command, make check_mode: false
                  - When use ansible.builtin.shell or ansible.builtin.command, make sure to quote the entire command string
                  - Use become: true when elevation is needed.
                  - Provide the following data as YAML, **without** wrapping it in triple backticks or markdown 
                    code fences. Do **not** include '```' or any additional formatting—just the raw YAML content.
                  - You must call the 'parse_yaml' tool with the YAML string after generating it. Do not parse YAML manually. Only use the tool.
                  - Do not attempt to parse YAML as Python code. Use the tool instead.
                  
                  Example format:
                  <code>
                  ---
                  - name: Example
                    hosts: all
                    tasks:
                      - name: hello
                        ansible.builtin.shell:
                          cmd: "echo hello"
                          check_mode: false
                        become: true
                  </code>
                  Task:
                  {task}
                """,

    "bash": """You are a Bash scripting assistant.
                Output only the final Bash script, no explanations or markdown formatting.
                Task:
                {task}
                """,

    "docker": """You are generating a Dockerfile.
                  Only output the Dockerfile content, no backticks or extra formatting.
                  Task:
                  {task}
                  """
}
