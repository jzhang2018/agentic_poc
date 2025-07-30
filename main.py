# main.py

from iac_agent.agent import generate_ansible_playbook

def main():
    task = "Write an Ansible playbook to set the hostname to 'webserver-01' on Red Hat Linux"
    print(f"Task: {task}\n")

    playbook = generate_ansible_playbook(task)

    print("Generated Ansible Playbook:\n")
    print(playbook)

if __name__ == "__main__":
    main()
