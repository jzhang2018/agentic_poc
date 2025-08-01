# prompts.py

PROMPT_TEMPLATES = {
    "ansible": """You are generating an Ansible YAML playbook.
                  Requirements:   
                  - Use native Ansible modules when possible.
                  - Use fully qualified collection names (e.g., ansible.builtin.shell).
                  - Use check_mode: false for all ansible.builtin.shell or ansible.builtin.command tasks.
                  - check_mode, become, and similar task-level attributes must be top-level keys within a task, not nested inside the module dictionary.
                  - When use ansible.builtin.shell or ansible.builtin.command, make sure to quote the entire command string
                  - Use become_user: root when the elevation is needed.
                  - Provide the following data as YAML, **without** wrapping it in triple backticks or markdown 
                    code fences. Do **not** include '```' or any additional formatting—just the raw YAML content.
                  - You MUST call the 'parse_yaml' tool with the YAML string after generating it. Do not parse YAML manually. Only use the tool. No exceptions!!!
                  - Do not attempt to parse YAML as Python code. Use the tool instead. No exceptions!!! 
                  - Also generate a minimal Ansible inventory that includes the following:
                    - A host with IP address {inventory_ip}
                    - Assign it to a group named [{inventory_group}]
                    - Use SSH user '{inventory_user}'
                    - Format the inventory as INI syntax, directly in the response as plain text after the playbook YAML
                  
                  - Your final_answer must return a Python dictionary using this structure:
                    final_answer({{
                      "playbook": [...parsed YAML...],
                      "inventory": "INI-formatted string (e.g. [group]\nhost ansible_host=...)"
                    }})

                  - The playbook should be returned as a list of dicts (parsed YAML).
                  - The inventory must be returned as a raw string (do not parse with parse_yaml).
                  - Do not return any Python code (e.g. no variable assignments like playbook_yaml = ...).
                  - Do not wrap output in markdown.  

                  Example inventory format:
                  [{inventory_group}]
                  host01 ansible_host={inventory_ip} ansible_user={inventory_user}
                  
                  Example playbook format:
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
