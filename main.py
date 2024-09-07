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
def import_patterns(file_name):
    module_name = file_name.replace('.py', '')
    spec = importlib.util.spec_from_file_location(module_name, file_name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.single_patterns


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


# Function to generate trading action advice
def generate_trading_action(pattern_name):
    actions = {
        "Doji": "This pattern indicates indecision in the market; look for confirmation near support or resistance levels.",
        "Bullish Marubozu": "This pattern suggests strong buying pressure; consider entering a long position if near support.",
        "Bearish Marubozu": "This pattern suggests strong selling pressure; consider entering a short position if near resistance.",
        "Hammer": "This pattern indicates a potential reversal; consider buying if it forms at a support level.",
        "Inverted Hammer": "This pattern may indicate a bullish reversal; look for confirmation near support.",
        "Shooting Star": "This pattern signals a potential bearish reversal; consider selling if it forms at resistance.",
        "Hanging Man": "This pattern suggests a potential reversal; consider selling if it forms at resistance."
    }
    return actions.get(pattern_name, "Analyze this pattern in conjunction with support and resistance levels.")


# Function to censor the pattern name in a given text
def censor_text(text, pattern_name):
    # Replace occurrences of the pattern name with "This pattern"
    return text.replace(f"The {pattern_name} pattern", "This pattern").replace(pattern_name, "This pattern")


# Function to generate explanations for each pattern
def generate_explanations(pattern_name):
    explanations = {
        "Doji": [
            "This pattern represents indecision in the market, as buyers and sellers are equally matched.",
            "The pattern suggests that the previous trend may be losing strength, and a reversal could be imminent.",
            "Traders often look for this pattern near support or resistance levels as a potential reversal signal."
        ],
        "Bullish Marubozu": [
            "This pattern shows strong buying interest, with no wicks indicating control by buyers throughout the period.",
            "The pattern forms when the open is at the low and the close is at the high, suggesting a continuation of a bullish trend.",
            "If this pattern appears near a support level, it could be a signal to enter a long position."
        ],
        "Bearish Marubozu": [
            "This pattern shows strong selling pressure, with no wicks indicating control by sellers throughout the period.",
            "The pattern forms when the open is at the high and the close is at the low, suggesting a continuation of a bearish trend.",
            "If this pattern appears near a resistance level, it could be a signal to enter a short position."
        ],
        "Hammer": [
            "This pattern suggests that a downtrend may be coming to an end, as buyers managed to push the price back up after a significant decline.",
            "The pattern often forms at the bottom of a downtrend and is characterized by a small body with a long lower wick.",
            "If this pattern forms near a support level, it can indicate a buying opportunity as it suggests the potential for a reversal."
        ],
        "Inverted Hammer": [
            "This pattern suggests a potential bullish reversal as it indicates buying pressure despite opening near the low of the session.",
            "The pattern is characterized by a long upper wick and a small body, signaling that buyers tried to push the price higher.",
            "If this pattern appears at the end of a downtrend, it could be an early sign of a bullish reversal."
        ],
        "Shooting Star": [
            "This pattern is a bearish signal that forms after an uptrend, indicating a potential reversal to the downside.",
            "The pattern has a small body near the low of the session with a long upper wick, suggesting that buyers were unable to maintain control.",
            "If this pattern forms at a resistance level, it could be a signal to consider shorting the market."
        ],
        "Hanging Man": [
            "This pattern is a bearish signal that forms at the top of an uptrend, indicating that selling pressure is increasing.",
            "The pattern is similar to the Hammer but occurs after a bullish trend, suggesting a potential reversal to the downside.",
            "Traders look for this pattern near resistance levels to signal a selling opportunity."
        ]
    }
    return explanations.get(pattern_name, ["This pattern indicates indecision in the market."])


# Function to generate a quiz based on selected patterns
def generate_quiz(candlestick_patterns):
    quiz_pool = []
    for category, ascii_art in candlestick_patterns.items():
        ascii_art_str = "\n".join(ascii_art)
        description = f"The {category} pattern is used to identify potential market reversals or trends."
        censored_description = censor_text(description, category)
        explanations = generate_explanations(category)
        quiz_pool.append((category, censored_description.capitalize(), ascii_art_str, explanations))
    random.shuffle(quiz_pool)  # Randomize the order of questions
    return quiz_pool


# Function to present the quiz
def present_quiz(quiz_pool):
    for i, (name, description, ascii_art, explanations) in enumerate(quiz_pool, 1):
        clear_screen()
        print(colored(f"Question {i}: ", 'magenta', attrs=['bold']) +
              colored("What is this candlestick pattern?", 'magenta', attrs=['underline']))
        print(colored(ascii_art, 'green', attrs=['bold']))
        print(Fore.CYAN + "\nOptions:" + Style.RESET_ALL)

        # Generate multiple-choice options for the pattern name
        options = random.sample(quiz_pool, min(3, len(quiz_pool)))  # Adjust number of options to the available pool size
        if (name, description, ascii_art, explanations) not in options:
            options[0] = (name, description, ascii_art, explanations)
        random.shuffle(options)  # Randomize the position of the correct answer

        correct_option = options.index((name, description, ascii_art, explanations))
        option_letters = ['a', 'b', 'c']
        for idx, (opt_name, _, _, _) in enumerate(options):
            print(f"{option_letters[idx]}. {opt_name}")

        user_answer = input(Fore.YELLOW + "Your answer: " + Style.RESET_ALL).strip().lower()
        if user_answer == option_letters[correct_option]:
            print(colored("\nCorrect!\n", 'green', attrs=['bold']))

            # Ask user to guess the explanation
            explanation_options = explanations.copy()
            random.shuffle(explanation_options)
            print(colored("Guess the Explanation:", 'cyan', attrs=['bold']))
            for idx, exp in enumerate(explanation_options):
                print(f"{option_letters[idx]}. {exp}")

            correct_explanation = explanation_options.index(explanations[0])
            user_explanation = input(Fore.YELLOW + "Your explanation: " + Style.RESET_ALL).strip().lower()
            if user_explanation == option_letters[correct_explanation]:
                print(colored("\nCorrect Explanation!\n", 'green', attrs=['bold']))

                # Ask user to guess the trading action
                trading_action = generate_trading_action(name)
                available_trading_actions = [
                    generate_trading_action(n) for n, _, _, _ in quiz_pool if n != name
                ]
                trading_options = [trading_action] + random.sample(
                    available_trading_actions, min(2, len(available_trading_actions))
                )
                random.shuffle(trading_options)
                print(colored("Guess the Trading Action:", 'cyan', attrs=['bold']))
                for idx, action in enumerate(trading_options):
                    print(f"{option_letters[idx]}. {action}")

                correct_action = trading_options.index(trading_action)
                user_action = input(Fore.YELLOW + "Your trading action: " + Style.RESET_ALL).strip().lower()
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
            patterns = import_patterns(file)
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
    quiz_pool = generate_quiz(candlestick_patterns)
    present_quiz(quiz_pool)


if __name__ == "__main__":
    main()
