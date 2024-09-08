import random
import os
import importlib.util

# ANSI escape codes for colors and styles
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
RESET = "\033[0m"

# Function to dynamically import a module from a given file path
def import_module(file_name):
    module_name = file_name.replace('.py', '')
    spec = importlib.util.spec_from_file_location(module_name, file_name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

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

# Function to find all .py files with 'pattern' or 'trader' in their name in the current directory
def find_pattern_files():
    pattern_files = [
        f for f in os.listdir('.') if f.endswith('.py') and f != os.path.basename(__file__) and ('pattern' in f.lower() or 'trader' in f.lower())
    ]
    # Sort files according to the specified hierarchy
    hierarchy = ['single', 'double', 'triple', 'continue', 'complex', 'trader']
    sorted_files = sorted(
        pattern_files,
        key=lambda x: next((i for i, h in enumerate(hierarchy) if h in x.lower()), len(hierarchy))
    )
    return sorted_files

# Function to convert file names to a more readable format
def convert_filename_to_display_name(filename):
    name = filename.replace('_', ' ').replace('.py', '')
    return name.title()

# Function to display the file selection menu and get user choice
def display_file_menu(pattern_files):
    while True:
        print(f"{CYAN}{BOLD}Select the pattern files to include in the quiz (type 'return' to go back, 'exit' to quit):{RESET}")
        for i, file in enumerate(pattern_files, 1):
            display_name = convert_filename_to_display_name(file)
            print(f"{i}. {display_name}")
        choices = get_input_with_exit(f"{YELLOW}\nEnter your choices (comma-separated) or 'exit' to quit: {RESET}").split(",")
        if choices is None:
            return None  # Go back to menu
        selected_files = [
            pattern_files[int(choice.strip()) - 1] for choice in choices
            if choice.strip().isdigit() and 1 <= int(choice.strip()) <= len(pattern_files)
        ]
        if selected_files:
            return selected_files
        else:
            print(f"{RED}No valid files selected. Try again.{RESET}")

# Function to censor the pattern name in a given text
def censor_text(text, pattern_name):
    return text.replace(f"The {pattern_name} pattern", "This pattern").replace(pattern_name, "This pattern")

# Function to generate a quiz based on selected patterns or trading terms
def generate_quiz(candlestick_patterns, explanations, trading_actions, trading_terms):
    quiz_pool = []

    # Add pattern questions
    for category, ascii_art in candlestick_patterns.items():
        ascii_art_str = "\n".join(ascii_art)
        description = f"The {category} pattern is used to identify potential market reversals or trends."
        censored_description = censor_text(description, category)
        explanation = explanations.get(category, ["This pattern indicates indecision in the market."])
        trading_action = trading_actions.get(category, "Analyze this pattern in conjunction with support and resistance levels.")
        quiz_pool.append((category, censored_description.capitalize(), ascii_art_str, explanation, trading_action))

    # Add jargon questions
    for term, definition in trading_terms.items():
        question = f"{RESET}What does {PURPLE}{UNDERLINE}{BOLD}{term}{RESET} mean?"
        correct_answer = definition
        # Ensure 2 incorrect answers from the rest of the terms
        incorrect_answers = random.sample([v for k, v in trading_terms.items() if k != term], 2)
        options = [correct_answer] + incorrect_answers
        random.shuffle(options)  # Shuffle options to randomize correct answer position
        quiz_pool.append((term, question, None, options, correct_answer))

    random.shuffle(quiz_pool)  # Randomize the order of questions
    return quiz_pool

# Function to select explanations with similar functions
def get_similar_explanations(correct_pattern, explanations_dict):
    similar_patterns = [key for key in explanations_dict if key != correct_pattern]
    incorrect_explanations = random.sample(similar_patterns, 2)  # Select 2 random other patterns
    return [explanations_dict[correct_pattern][0]] + [explanations_dict[pattern][0] for pattern in incorrect_explanations]

# Function to present the quiz
def present_quiz(quiz_pool, explanations):
    for i, (name, description, ascii_art, options, correct_answer) in enumerate(quiz_pool, 1):
        clear_screen()
        if ascii_art:  # If ascii_art is present, it's a candlestick pattern question
            print(f"\n{PURPLE}{BOLD}{UNDERLINE}{'What is this candlestick pattern?'}\n")
            print(f"{GREEN}{BOLD}{ascii_art}{RESET}")
            print(f"{CYAN}\nOptions:\n{RESET}")
        else:  # It's a jargon question
            print(f"\n{PURPLE}{BOLD}{UNDERLINE}{description.ljust(60, ' ')}{RESET}\n")
            print(f"{CYAN}\nOptions:\n{RESET}")

        option_letters = ['A', 'B', 'C']
        for idx, opt in enumerate(options):
            print(f"{option_letters[idx]}. {opt}")

        user_answer = get_input_with_exit(f"\n{YELLOW}Your answer (or 'return' to go back, 'exit' to quit): {RESET}")
        if user_answer is None:  # User chose to return to the menu
            return
        user_answer = user_answer.upper()

        if correct_answer in options and user_answer == option_letters[options.index(correct_answer)]:
            print(f"{GREEN}{BOLD}\nCorrect!\n{RESET}")
        else:
            print(f"{LIGHT_RED}{ITALIC}{BOLD}\nWrong!\n\nThe correct answer is:\n{RESET}{RED}{UNDERLINE}{BOLD}{correct_answer}{RESET}\n")

        next_step = get_input_with_exit(f"{YELLOW}Press Enter to continue or type 'return' to go back, 'exit' to quit: {RESET}")
        if next_step is None:  # User chose to return to the menu
            return

# Main function to run the quiz
def main():
    while True:
        clear_screen()

        # Import explanations and trading actions from separate files
        explanations_module = import_module('explanation.py')
        trading_actions_module = import_module('trading_actions.py')

        explanations = explanations_module.explanations
        trading_actions = trading_actions_module.trading_actions

        # Step 1: Find all .py pattern files in the current directory
        pattern_files = find_pattern_files()
        if not pattern_files:
            print(f"{RED}No pattern files found. Exiting...{RESET}")
            return

        # Step 2: User selects which pattern files to use
        selected_files = display_file_menu(pattern_files)
        if selected_files is None:  # Go back to menu
            continue
        if not selected_files:
            print(f"{RED}No valid files selected. Exiting...{RESET}")
            return

        # Step 3: Load patterns or terms from selected files
        candlestick_patterns = {}
        trading_terms = {}
        for file in selected_files:
            try:
                module = import_module(file)
                if hasattr(module, 'patterns'):
                    # Handle pattern files
                    candlestick_patterns.update(module.patterns)
                elif hasattr(module, 'trading_terms'):
                    # Handle trader's dictionary file
                    trading_terms.update(module.trading_terms)
                else:
                    print(f"{YELLOW}File '{file}' does not contain recognizable data for this quiz.{RESET}")
            except FileNotFoundError as e:
                print(f"{RED}Error loading {file}: {e}{RESET}")
                continue
            except ImportError as e:
                print(f"{RED}Error loading {file}: {e}{RESET}")
                continue
        if not candlestick_patterns and not trading_terms:
            print(f"{RED}No patterns or terms loaded. Exiting...{RESET}")
            return

        # Step 4: Generate and present the quiz
        quiz_pool = generate_quiz(candlestick_patterns, explanations, trading_actions, trading_terms)
        present_quiz(quiz_pool, explanations)

if __name__ == "__main__":
    main()
