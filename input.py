def ask_choice(prompt: str, choices: list[str]) -> str:
    while True:
        options = ",".join(choices)
        choice = input(f"{prompt} ({options}): ")
        if choice in choices:
            return choice

def ask_yes_no(prompt: str) -> bool:
    while True:
        choice = input(prompt).lower()
        if choice in ["y", "yes"]:
            return True
        elif choice in ["n", "no"]:
            return False


