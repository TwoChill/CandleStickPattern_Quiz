"""
Candlestick Pattern Quiz Script

This script dynamically imports candlestick pattern files, presents a quiz to the user to identify patterns,
and provides explanations and trading actions based on user responses.
"""

import random
import os
import importlib.util
from colorama import init, Fore, Style
from termcolor import colored

# Initialize colorama for Windows compatibility and auto-reset
init(autoreset=True)

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

# Function to find all .py files in the current directory
def find_pattern_files():
    pattern_files = [
        f for f in os.listdir('.') if f.endswith('.py') and f != os.path.basename(__file__)
    ]
    # Sort files according to the specified hierarchy
    hierarchy = ['single', 'double', 'triple', 'continue', 'complex']
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
    print(colored("Select the pattern files to include in the quiz:", 'cyan', attrs=['bold']))
    for i, file in enumerate(pattern_files, 1):
        display_name = convert_filename_to_display_name(file)
        print(f"{i}. {display_name}")
    choices = input(Fore.YELLOW + "\nEnter your choices (comma-separated): " + Style.RESET_ALL).split(",")
    selected_files = [
        pattern_files[int(choice.strip()) - 1] for choice in choices
        if choice.strip().isdigit() and 1 <= int(choice.strip()) <= len(pattern_files)
    ]
    return selected_files

# Function to censor the pattern name in a given text
def censor_text(text, pattern_name):
    # Replace occurrences of the pattern name with "This pattern"
    return text.replace(f"The {pattern_name} pattern", "This pattern").replace(pattern_name, "This pattern")

# Function to generate a quiz based on selected patterns
def generate_quiz(candlestick_patterns, explanations, trading_actions):
    quiz_pool = []
    for category, ascii_art in candlestick_patterns.items():
        ascii_art_str = "\n".join(ascii_art)
        description = f"The {category} pattern is used to identify potential market reversals or trends."
        censored_description = censor_text(description, category)
        explanation = explanations.get(category, ["This pattern indicates indecision in the market."])
        trading_action = trading_actions.get(category, "Analyze this pattern in conjunction with support and resistance levels.")
        quiz_pool.append((category, censored_description.capitalize(), ascii_art_str, explanation, trading_action))
    random.shuffle(quiz_pool)  # Randomize the order of questions
    return quiz_pool

# Function to present the quiz
def present_quiz(quiz_pool):
    for i, (name, description, ascii_art, explanations, trading_action) in enumerate(quiz_pool, 1):
        clear_screen()
        print(colored(f"Question {i}: ", 'magenta', attrs=['bold']) +
              colored("What is this candlestick pattern?", 'magenta', attrs=['underline']))
        print(colored(ascii_art, 'green', attrs=['bold']))
        print(Fore.CYAN + "\nOptions:" + Style.RESET_ALL)

        # Generate multiple-choice options for the pattern name
        options = random.sample(quiz_pool, min(5, len(quiz_pool)))  # Adjust number of options to 5
        if (name, description, ascii_art, explanations, trading_action) not in options:
            options[0] = (name, description, ascii_art, explanations, trading_action)
        random.shuffle(options)  # Randomize the position of the correct answer

        correct_option = options.index((name, description, ascii_art, explanations, trading_action))
        option_letters = ['A', 'B', 'C', 'D', 'E']
        for idx, (opt_name, _, _, _, _) in enumerate(options):
            print(f"{option_letters[idx]}. {opt_name}")

        user_answer = input(Fore.YELLOW + "Your answer: " + Style.RESET_ALL).strip().upper()
        if user_answer == option_letters[correct_option]:
            print(colored("\nCorrect!\n", 'green', attrs=['bold']))

            # Ask user to guess the explanation
            explanation_options = explanations.copy()
            random.shuffle(explanation_options)
            print(colored("Guess the Explanation:", 'cyan', attrs=['bold']))
            for idx, exp in enumerate(explanation_options[:5]):  # Ensure only 5 options
                print(f"{option_letters[idx]}. {exp}")

            correct_explanation = explanation_options.index(explanations[0])
            user_explanation = input(Fore.YELLOW + "Your explanation: " + Style.RESET_ALL).strip().upper()
            if user_explanation == option_letters[correct_explanation]:
                print(colored("\nCorrect Explanation!\n", 'green', attrs=['bold']))

                # Ask user to guess the trading action
                # Ensure trading actions are kept separate and distinct
                trading_options = [trading_action]
                available_trading_actions = [
                    action for name, _, _, _, action in quiz_pool if action != trading_action
                ]
                trading_options += random.sample(
                    available_trading_actions, min(4, len(available_trading_actions))
                )  # Limit to 5 options total
                random.shuffle(trading_options)
                print(colored("Guess the Trading Action:", 'cyan', attrs=['bold']))
                for idx, action in enumerate(trading_options):
                    print(f"{option_letters[idx]}. {action}")

                correct_action = trading_options.index(trading_action)
                user_action = input(Fore.YELLOW + "Your trading action: " + Style.RESET_ALL).strip().upper()
                if user_action == option_letters[correct_action]:
                    print(colored("\nCorrect Trading Action!\n", 'green', attrs=['bold']))
                else:
                    print(colored(f"\nWrong Trading Action! The correct action is: {trading_action}\n", 'red', attrs=['bold']))
            else:
                print(colored(f"\nWrong Explanation! The correct explanation is: {explanations[0]}\n", 'red', attrs=['bold']))
        else:
            print(colored(f"\nWrong! The correct answer is: {name}\n", 'red', attrs=['bold']))

        input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)

# Main function to run the quiz
def main():
    clear_screen()

    # Import explanations and trading actions from separate files
    explanations_module = import_module('explanation.py')
    trading_actions_module = import_module('trading_actions.py')

    explanations = explanations_module.explanations
    trading_actions = trading_actions_module.trading_actions

    # Step 1: Find all .py pattern files in the current directory
    pattern_files = find_pattern_files()
    if not pattern_files:
        print(Fore.RED + "No pattern files found. Exiting..." + Style.RESET_ALL)
        return

    # Step 2: User selects which pattern files to use
    selected_files = display_file_menu(pattern_files)
    if not selected_files:
        print(Fore.RED + "No valid files selected. Exiting..." + Style.RESET_ALL)
        return

    # Step 3: Load patterns from selected files
    candlestick_patterns = {}
    for file in selected_files:
        try:
            patterns = import_module(file).single_patterns
            candlestick_patterns.update(patterns)
        except FileNotFoundError as e:
            print(Fore.RED + f"Error loading {file}: {e}" + Style.RESET_ALL)
            continue
        except ImportError as e:
            print(Fore.RED + f"Error loading {file}: {e}" + Style.RESET_ALL)
            continue

    if not candlestick_patterns:
        print(Fore.RED + "No patterns loaded. Exiting..." + Style.RESET_ALL)
        return

    # Step 4: Generate and present the quiz
    quiz_pool = generate_quiz(candlestick_patterns, explanations, trading_actions)
    present_quiz(quiz_pool)

if __name__ == "__main__":
    main()
