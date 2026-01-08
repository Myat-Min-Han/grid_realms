from colorama import Fore, Style

#choice
def ask_yes_no(prompt: str) -> bool:
    while True:
        choice = input(prompt).strip().lower()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print("> Invalid input. Please enter 'yes' or 'no'.")

def get_choice(prompt: str, options: list[str]) -> str:
    options_str = "/".join(options)
    while True:
        choice = input(f"{prompt} ({options_str}): ").strip()
        if choice in options:
            return choice
        else:
            print(f"> Invalid input. Please choose from: {options_str}.")


def ask_still_playing() -> bool:
    return ask_yes_no(f"{Fore.YELLOW}> Do you want to continue playing? (yes/no): {Style.RESET_ALL}")

