from iac_agent.agent import generate_ansible_playbook

def test_generate_ansible_playbook():
    task = "Write an ansible playbook to Set hostname to 'webserver-01' on Red Hat Linux"
    result = generate_ansible_playbook(task)

    print(result)
    assert isinstance(result, str)
    assert "hostname" in result.lower()
