# executor/dry_run_ansible.py

import tempfile
import subprocess
import os, re, yaml, ast

def sanitize_playbook(runbook):
    """Sanitize commands in the playbook by removing surrounding quotes from strings."""
    if not isinstance(runbook, dict):
        return runbook

    playbook = runbook.get("playbook")
    if not isinstance(playbook, list):
        return runbook

    for play in playbook:
        tasks = play.get("tasks", [])
        for task in tasks:
            for module_name, module_args in task.items():
                if isinstance(module_args, dict):
                    for key in ['cmd', '_raw_params']:
                        if key in module_args and isinstance(module_args[key], str):
                            val = module_args[key].strip()
                            if val.startswith('"') and val.endswith('"'):
                                module_args[key] = val[1:-1]
    return runbook

def split_playbook_and_inventory(runbook_obj) -> tuple[str, str]:
    """
    Expects a dict-like object with 'playbook' and 'inventory' keys.
    Falls back to literal_eval if needed.
    """
    raw_text = str(runbook_obj)
    print("👉👉 raw_text:\n" + raw_text + "👈👈")

    # 1. Try literal_eval for Python dict-style final_answer
    try:
        parsed = ast.literal_eval(raw_text)
        if isinstance(parsed, dict) and "playbook" in parsed and "inventory" in parsed:
            playbook_yaml = yaml.dump(parsed["playbook"], sort_keys=False)
            return playbook_yaml.strip(), parsed["inventory"].strip()
    except Exception as e:
        print(f"[Fallback Parsing Error] {e}")

    # 2. Legacy fallback: regex for raw strings inside final_answer(...)
    match = re.search(r"final_answer\s*\(\s*(\{.*\})\s*\)", raw_text, re.DOTALL)
    if match:
        try:
            parsed = ast.literal_eval(match.group(1))
            if isinstance(parsed, dict) and "playbook" in parsed and "inventory" in parsed:
                playbook_yaml = yaml.dump(parsed["playbook"], sort_keys=False)
                return playbook_yaml.strip(), parsed["inventory"].strip()
        except Exception as e:
            print(f"[Regex fallback parsing error] {e}")

    raise ValueError("Could not extract both playbook and inventory from runbook.")

def ansible_dry_run(runbook) -> str:
    """
    Takes a runbook (AgentText or str), extracts playbook/inventory, and performs dry run.
    """
    # Sanitize runbook
    sanitized_runbook = sanitize_playbook(runbook)
    
    playbook_str, inventory_str = split_playbook_and_inventory(sanitized_runbook)

    print("Playbook 👉👉\n" + playbook_str + "\n👈👈")
    print("Inventory 👉👉\n" + inventory_str + "\n👈👈")

    with tempfile.NamedTemporaryFile(mode='w+', suffix=".yml", delete=False) as playbook_file, \
         tempfile.NamedTemporaryFile(mode='w+', suffix=".ini", delete=False) as inventory_file:
        
        playbook_file.write(playbook_str)
        inventory_file.write(inventory_str)

        safe_tmp_dir = "/var/tmp/ansible_run"        
        os.makedirs(safe_tmp_dir, exist_ok=True)

        playbook_path = os.path.join(safe_tmp_dir, "playbook.yml")
        inventory_path = os.path.join(safe_tmp_dir, "inventory.ini")

        with open(playbook_path, "w") as playbook_file:
            playbook_file.write(playbook_str)

        with open(inventory_path, "w") as inventory_file:
            inventory_file.write(inventory_str)

        print("Playbook file path 👉👉\n" + playbook_path + "\n👈👈")
        print("Inventory file path 👉👉\n" + inventory_path + "\n👈👈")

    try:
        result = subprocess.run(
            ["ansible-playbook", "--check", "-i", inventory_path, playbook_path, "--ask-pass"],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout + result.stderr

    finally:
        os.remove(playbook_path)
        os.remove(inventory_path)
