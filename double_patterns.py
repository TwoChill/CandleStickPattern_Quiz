from colorama import init, Fore

# Initialize colorama for color support in terminal
init(autoreset=True)

# DEBUG = True
DEBUG = False

# Double Candlestick Patterns
patterns = {
    "Bullish Engulfing": [
        f'                        ',
        f'                {Fore.GREEN}║{Fore.RESET}            ',
        f'      {Fore.RED}║{Fore.RESET}     {Fore.GREEN}|███████|{Fore.RESET}        ',
        f'  {Fore.RED}|███████|{Fore.RESET} {Fore.GREEN}|███████|{Fore.RESET}        ',
        f'  {Fore.RED}|███████|{Fore.RESET} {Fore.GREEN}|███████|{Fore.RESET}        ',
        f'  {Fore.RED}|███████|{Fore.RESET} {Fore.GREEN}|███████|{Fore.RESET}        ',
        f'  {Fore.RED}|███████|{Fore.RESET} {Fore.GREEN}|███████|{Fore.RESET}        ',
        f'      {Fore.RED}║{Fore.RESET}     {Fore.GREEN}|███████|{Fore.RESET}        ',
        f'                {Fore.GREEN}║{Fore.RESET}            ',
        f'                        '
    ],
    "Bearish Engulfing": [
        f'                        ',
        f'                {Fore.RED}║{Fore.RESET}            ',
        f'      {Fore.GREEN}║{Fore.RESET}     {Fore.RED}|███████|{Fore.RESET}        ',
        f'  {Fore.GREEN}|███████|{Fore.RESET} {Fore.RED}|███████|{Fore.RESET}        ',
        f'  {Fore.GREEN}|███████|{Fore.RESET} {Fore.RED}|███████|{Fore.RESET}        ',
        f'  {Fore.GREEN}|███████|{Fore.RESET} {Fore.RED}|███████|{Fore.RESET}        ',
        f'  {Fore.GREEN}|███████|{Fore.RESET} {Fore.RED}|███████|{Fore.RESET}        ',
        f'      {Fore.GREEN}║{Fore.RESET}     {Fore.RED}|███████|{Fore.RESET}        ',
        f'                {Fore.RED}║{Fore.RESET}            ',
        f'                        '
    ]
}

def draw_double_patterns():
    for pattern, art in patterns.items():
        print(f'\n{pattern}:\n' + '\n'.join(art))

# Call the function to display double candlestick patterns
if __name__ == '__main__':
    if DEBUG:
        draw_double_patterns()
