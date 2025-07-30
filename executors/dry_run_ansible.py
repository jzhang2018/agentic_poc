# executors/dry_run_ansible.py

import tempfile
import subprocess
import os
import yaml

def patch_playbook_for_localhost(playbook_str: str) -> str:
    """
    Patch the playbook string to ensure safe dry run:
    - Set hosts to localhost
    - Set connection to local
    - Disable facts gathering
    """
    try:
        docs = yaml.safe_load(playbook_str)
    except yaml.YAMLError as e:
        raise ValueError(f"Invalid YAML in playbook: {e}")

    # If the playbook is a list of plays (common structure)
    if isinstance(docs, list):
        for play in docs:
            if isinstance(play, dict):
                play["hosts"] = "localhost"
                play["connection"] = "local"
                play["gather_facts"] = False
    else:
        raise ValueError("Playbook content is not a list of plays")

    return yaml.dump(docs, sort_keys=False)

def ansible_dry_run(playbook_str: str) -> str:
    """
    Perform a dry run of the given Ansible playbook after patching it.

    Args:
        playbook_str (str): The playbook content as a string.

    Returns:
        str: Output from the Ansible dry run.
    """
    patched_playbook = patch_playbook_for_localhost(playbook_str)

    print("++++++++++++++++++++++++ Patched playbook: ")
    print(patched_playbook)

    with tempfile.NamedTemporaryFile(mode='w+', suffix=".yml", delete=False) as temp_file:
        temp_file.write(patched_playbook)
        temp_file_path = temp_file.name

    try:
        result = subprocess.run(
            ["ansible-playbook", "--check", temp_file_path],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout + result.stderr

    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
