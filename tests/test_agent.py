from iac_agent.agent import generate_ansible_playbook

def test_generate_ansible_playbook():
    task = "Write an Ansible playbook to fix the swap space full on Red Hat Linux VM"
    result = generate_ansible_playbook(task)

    print(result)
    assert isinstance(result, str)
    assert "hostname" in result.lower()
