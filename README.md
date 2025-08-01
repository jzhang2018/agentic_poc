This is a POC for agentic ai exercise. The end-to-end use case is:

                    +----------------------+
                    |  Monitoring Tool     |
                    | (e.g., Prometheus,   |
                    |  custom script, etc) |
                    +---------+------------+
                              |
                              v
                    +---------+------------+
                    |  Event Queue         |
                    | (e.g., Redis, MQTT)  |
                    +---------+------------+
                              |
                              v
                    +---------+--------------+
                    | Agent Listener (Python)|
                    | - Subscribes to queue  |
                    | - Triggers action      |
                    +---------+--------------+
                              |
                              v  <-------------- POC starts here
                    +---------+------------+
                    |  SmolAgent + LiteLLM |
                    |     (w/openai/       | 
                    |     gpt-3.5-turbo)   |
                    |   - Prompt LLM       |
                    |   - Generate fix     |
                    +---------+------------+
                              |
                              v
                    +---------+------------+
                    |  Ansible Executor    |
                    | - Save playbook.yaml |
                    | - Run it w/ Ansible  |
                    +----------------------+

Design Pattern:  Feedback-Driven Agent Loop </br>
Task → LLM Reasoning (Parsed Plan → Code) → Code Output  → Dry Run → Evaluate → [ Success ✅ | Feedback ❌ → Retry ] </br>

Goal-driven and technology-agnostic agent architecture </br>
