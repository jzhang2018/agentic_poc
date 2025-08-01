# main.py

from iac_agent.agent import generate_runbook
from utils.dry_run_dispatcher import run_dry_run
from prompts import PROMPT_TEMPLATES

def build_prompt(technology, task):
    template = PROMPT_TEMPLATES.get(technology)
    if not template:
        raise ValueError(f"No prompt template for {technology}")
    return template.format(task=task)

def main():
    # task = """
    #     Write a clean, idiomatic Ansible playbook to fix the swap space full issue on a Red Hat Linux VM.

    #     Requirements:
    #     - Use native Ansible modules when possible.
    #     - When use ansible.builtin.shell or ansible.builtin.command, make check_mode: false
    #     - When use ansible.builtin.shell or ansible.builtin.command, make sure to quote the entire command string
    #     - If privilege needs to be elavated, set become: true
    #     - Output only valid plain YAML syntax and structure, suitable for direct parsing by a YAML parser.
    #     - Provide the following data as YAML, **without** wrapping it in triple backticks or 
    #         markdown code fences. Do **not** include '---' or any additional formatting—just the raw YAML content.
    #     - Structure it according to Ansible's expected format, such as:
    #         - name: ...
    #           hosts: ...
    #           tasks:
    #             - name: ...
    #             ...
    #     """

    task = build_prompt("ansible", "Write a clean, idiomaticAnsible playbook to fix the swap space full issue on a Red Hat Linux VM.")
    print(f"++++++++++ Task: {task}\n")

    runbook = generate_runbook(task)
    print(f"++++++++++ Generated runbook:\n{runbook}")

    # print(playbook)

    # Now do a dry run or further processing
    # dry_run_result = run_dry_run("ansible", playbook)

    # print("\nDry Run Result:\n")
    # print(dry_run_result)

if __name__ == "__main__":
    main()
