# main.py

from iac_agent.agent import generate_ansible_playbook
from utils.dry_run_dispatcher import run_dry_run

def main():
    task = """
        Write a clean, idiomatic Ansible playbook to fix the swap space full issue on a Red Hat Linux VM.

        Requirements:
        - Use native Ansible modules when possible.
        - When use ansible.builtin.shell or ansible.builtin.command, make check_mode: false
        - If privilege needs to be elavated, set become: true
        - Provide valid YAML syntax with comments.
        - Do NOT wrap in markdown or triple backticks.
        - Do NOT include any explanatory text or preamble.
        - Only output the Ansible playbook in YAML format.
        """

    print(f"Task: {task}\n")

    playbook = generate_ansible_playbook(task)

    print("Generated Ansible Playbook:\n")
    print(playbook)

    # Now do a dry run or further processing
    dry_run_result = run_dry_run("ansible", playbook)

    print("\nDry Run Result:\n")
    print(dry_run_result)

if __name__ == "__main__":
    main()
