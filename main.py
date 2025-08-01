# main.py

from iac_agent.agent import generate_runbook
from utils.dry_run_dispatcher import run_dry_run
from prompts import PROMPT_TEMPLATES

def build_ansible_prompt(task, inventory_ip, inventory_user, inventory_group):
    return PROMPT_TEMPLATES["ansible"].format(
        task=task,
        inventory_ip=inventory_ip,
        inventory_user=inventory_user,
        inventory_group=inventory_group
)

def main():
    # build prompt
    prompt = build_ansible_prompt(
        task = "Write a clean, idiomaticAnsible playbook " +
            "to fix disk full issue on Linux server. Make sure no critical data is deleted.",
        inventory_ip="192.168.184.143",
        inventory_user="iacuser",
        inventory_group="ai_lab"
    )

    runbook = generate_runbook(prompt)
    print(f"Generated runbook:\n👉👉\n{str(runbook)}\n👈👈\n")

    # dry run
    dry_run_result = run_dry_run("ansible", str(runbook))

    print("\nDry Run Result:")
    print(dry_run_result)

    # execution
    

if __name__ == "__main__":
    main()
