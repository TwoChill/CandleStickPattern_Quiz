import random
import os
import importlib.util
from colorama import init

# Initialize colorama for color support in the terminal
init(autoreset=True)

# ANSI escape codes for colors and styles
RED = "\033[0;31m"
GREEN = "\033[0;32m"
CYAN = "\033[0;36m"
YELLOW = "\033[1;33m"
PURPLE = "\033[0;35m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"

# Function to dynamically import a module from a given file path
def import_module(file_name):
    try:
        module_name = file_name.replace('.py', '')
        spec = importlib.util.spec_from_file_location(module_name, file_name)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    except (FileNotFoundError, ImportError) as e:
        print(f"{RED}Error importing {file_name}: {e}{RESET}")
        return None

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to handle user input and check for exit or return commands
def get_input_with_exit(prompt):
    user_input = input(prompt).strip().lower()
    if user_input == 'exit':
        print(f"{RED}{BOLD}\nExiting the quiz. Goodbye!{RESET}")
        exit()
    elif user_input == 'return':
        return None  # Indicates to return to the menu
    return user_input

# Function to display the pattern name guessing quiz
def pattern_name_quiz(candlestick_patterns):
    pattern_names = list(candlestick_patterns.keys())
    correct_pattern = random.choice(pattern_names)
    correct_art = candlestick_patterns[correct_pattern]

    # Generate closely resembling names
    incorrect_names = random.sample([name for name in pattern_names if name != correct_pattern], 4)
    options = [correct_pattern] + incorrect_names
    random.shuffle(options)

    clear_screen()
    print(f"\n{PURPLE}{BOLD}{UNDERLINE}What candlestick pattern is this?{RESET}\n")
    print(f"{GREEN}{BOLD}\n" + "\n".join(correct_art) + f"\n{RESET}")

    print(f"{CYAN}\nOptions:\n{RESET}")
    option_letters = ['A', 'B', 'C', 'D', 'E']
    for idx, opt in enumerate(options):
        print(f"{option_letters[idx]}. {opt}")

    user_answer = get_input_with_exit(f"\n{YELLOW}Your answer (or 'return' to go back, 'exit' to quit): {RESET}")
    if user_answer is None:
        return
    user_answer = user_answer.upper()

    if correct_pattern in options and user_answer == option_letters[options.index(correct_pattern)]:
        print(f"{GREEN}{BOLD}\nCorrect! The pattern is {correct_pattern}.\n{RESET}")
    else:
        print(f"{RED}{ITALIC}{BOLD}\nWrong! The correct answer is: {RESET}{GREEN}{UNDERLINE}{BOLD}{correct_pattern}{RESET}\n")

    next_step = get_input_with_exit(f"{YELLOW}Press Enter to continue or type 'return' to go back, 'exit' to quit: {RESET}")
    if next_step is None:
        return

# Main function to run the quiz
def main():
    while True:
        clear_screen()

        # Import patterns from the 'single_patterns.py' file
        patterns_module = import_module('single_patterns.py')

        if patterns_module is None:
            continue  # Retry the loop if module fails to import

        candlestick_patterns = patterns_module.patterns

        if not candlestick_patterns:
            print(f"{RED}No patterns loaded. Exiting...{RESET}")
            return

        # Step 4: Present the quiz
        pattern_name_quiz(candlestick_patterns)

if __name__ == "__main__":
    main()
