# utils/dry_run_dispatcher.py

from executors.dry_run_ansible import ansible_dry_run

def run_dry_run(task_type: str, content: str) -> str:
    """
    Dispatch dry run based on task type.

    Args:
        task_type (str): The type of the task, e.g., 'ansible', 'terraform', etc.
        content (str): The content to be validated/executed in dry-run mode.

    Returns:
        str: Result of the dry run.
    """
    dispatch_map = {
        "ansible": ansible_dry_run
        # Future types:
        # "terraform": terraform_dry_run,
        # "docker": docker_dry_run,
    }

    dry_run_func = dispatch_map.get(task_type.lower())
    if not dry_run_func:
        raise ValueError(f"No dry run handler found for task type '{task_type}'")

    return dry_run_func(content)
