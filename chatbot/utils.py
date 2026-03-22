import re

def print_response(response):
    """
    Prints a formatted chatbot response with color-coded roles.

    Parameters:
        response (dict): {'role': 'assistant'/'user', 'content': str}
    """
    # ANSI escape codes
    BOLD = "\033[1m"
    BLUE = "\033[34m"
    GREEN = "\033[32m"
    MAGENTA = "\033[35m"  # for unknown roles
    RESET = "\033[0m"

    role = response.get('role', 'unknown')
    content = response.get('content', '')

    if role == 'assistant':
        color = GREEN
    elif role == 'user':
        color = BLUE
    else:
        color = MAGENTA

    print(f"{BOLD}{color}{role.capitalize()}{RESET}: {content}")


def clean_response(text: str) -> str:
    if "</think>" in text:
        text = text.split("</think>")[-1]
    return text.strip()