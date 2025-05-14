def log_conversation(agent_name, message):
    with open(f"{agent_name}_log.txt", "a", encoding="utf-8") as f:
        f.write(message + "\n\n")
