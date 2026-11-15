import os

# Vyčištění terminálu
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_enter(text="\n[ENTER] - Pokračovat"):
    input(text)

def print_title(title: str, width=50):
    print("=" * width)
    print(title.center(width))
    print("=" * width)
    print()