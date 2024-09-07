from colorama import init, Fore

# Initialize colorama for color support in terminal
init(autoreset=True)

DEBUG = False

patterns = {
    "Hammer": [
        f'                        ',
        f'            {Fore.GREEN}║{Fore.RESET}            ',
        f'            {Fore.GREEN}║{Fore.RESET}            ',
        f'            {Fore.GREEN}║{Fore.RESET}            ',
        f'            {Fore.GREEN}║{Fore.RESET}            ',
        f'            {Fore.GREEN}║{Fore.RESET}            ',
        f'            {Fore.GREEN}║{Fore.RESET}            ',
        f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
        f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
        f'                        '
    ],
    "Inverted Hammer": [
        f'                        ',
        f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
        f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
        f'            {Fore.GREEN}║{Fore.RESET}            ',
        f'            {Fore.GREEN}║{Fore.RESET}            ',
        f'            {Fore.GREEN}║{Fore.RESET}            ',
        f'            {Fore.GREEN}║{Fore.RESET}            ',
        f'            {Fore.GREEN}║{Fore.RESET}            ',
        f'            {Fore.GREEN}║{Fore.RESET}            ',
        f'                        '
    ],
    "Shooting Star": [
        f'                        ',
        f'        {Fore.RED}|███████|{Fore.RESET}        ',
        f'        {Fore.RED}|███████|{Fore.RESET}        ',
        f'            {Fore.RED}║{Fore.RESET}            ',
        f'            {Fore.RED}║{Fore.RESET}            ',
        f'            {Fore.RED}║{Fore.RESET}            ',
        f'            {Fore.RED}║{Fore.RESET}            ',
        f'            {Fore.RED}║{Fore.RESET}            ',
        f'            {Fore.RED}║{Fore.RESET}            ',
        f'                        '
    ],
    "Hanging Man": [
        f'                        ',
        f'            {Fore.RED}║{Fore.RESET}            ',
        f'            {Fore.RED}║{Fore.RESET}            ',
        f'            {Fore.RED}║{Fore.RESET}            ',
        f'            {Fore.RED}║{Fore.RESET}            ',
        f'            {Fore.RED}║{Fore.RESET}            ',
        f'            {Fore.RED}║{Fore.RESET}            ',
        f'        {Fore.RED}|███████|{Fore.RESET}        ',
        f'        {Fore.RED}|███████|{Fore.RESET}        ',
        f'                        '
    ],
    "Doji": [
        f'                        ',
        f'            {Fore.YELLOW}║{Fore.RESET}            ',
        f'            {Fore.YELLOW}║{Fore.RESET}            ',
        f'        {Fore.YELLOW}|███████|{Fore.RESET}        ',
        f'            {Fore.YELLOW}║{Fore.RESET}            ',
        f'            {Fore.YELLOW}║{Fore.RESET}            ',

        f'                        '
    ],
    "Long-legged Doji": [
        f'                        ',
        f'            {Fore.YELLOW}║{Fore.RESET}            ',
        f'            {Fore.YELLOW}║{Fore.RESET}            ',
        f'            {Fore.YELLOW}║{Fore.RESET}            ',
        f'            {Fore.YELLOW}║{Fore.RESET}            ',
        f'        {Fore.YELLOW}|███████|{Fore.RESET}        ',
        f'            {Fore.YELLOW}║{Fore.RESET}            ',
        f'            {Fore.YELLOW}║{Fore.RESET}            ',
        f'            {Fore.YELLOW}║{Fore.RESET}            ',
        f'            {Fore.YELLOW}║{Fore.RESET}            ',
        f'                        '
    ],
    "Gravestone Doji": [
        f'                        ',
        f'            {Fore.YELLOW}║{Fore.RESET}            ',
        f'            {Fore.YELLOW}║{Fore.RESET}            ',
        f'            {Fore.YELLOW}║{Fore.RESET}            ',
        f'            {Fore.YELLOW}║{Fore.RESET}            ',
        f'            {Fore.YELLOW}║{Fore.RESET}            ',
        f'            {Fore.YELLOW}║{Fore.RESET}            ',
        f'        {Fore.YELLOW}|███████|{Fore.RESET}        ',
        f'                        '
    ],
    "Dragonfly Doji": [
        f'                        ',
        f'        {Fore.YELLOW}|███████|{Fore.RESET}        ',
        f'            {Fore.YELLOW}║{Fore.RESET}            ',
        f'            {Fore.YELLOW}║{Fore.RESET}            ',
        f'            {Fore.YELLOW}║{Fore.RESET}            ',
        f'            {Fore.YELLOW}║{Fore.RESET}            ',
        f'            {Fore.YELLOW}║{Fore.RESET}            ',
        f'            {Fore.YELLOW}║{Fore.RESET}            ',
        f'            {Fore.YELLOW}║{Fore.RESET}            ',

        f'                        '
    ],
    "Bullish Marubozu": [
        f'                        ',
        f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
        f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
        f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
        f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
        f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
        f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
        f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
        f'                        '
    ],
    "Bullish Closing Marubozu": [
        f'                        ',
        f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
        f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
        f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
        f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
        f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
        f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
        f'            {Fore.GREEN}║{Fore.RESET}            ',


        f'                        '
    ],
    "Bullish Opening Marubozu": [
        f'                        ',

        f'            {Fore.GREEN}║{Fore.RESET}            ',
        f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
        f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
        f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
        f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
        f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
        f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
        f'                        '
    ],
    "Bearish Marubozu": [
        f'                        ',
        f'        {Fore.RED}|███████|{Fore.RESET}        ',
        f'        {Fore.RED}|███████|{Fore.RESET}        ',
        f'        {Fore.RED}|███████|{Fore.RESET}        ',
        f'        {Fore.RED}|███████|{Fore.RESET}        ',
        f'        {Fore.RED}|███████|{Fore.RESET}        ',
        f'        {Fore.RED}|███████|{Fore.RESET}        ',
        f'        {Fore.RED}|███████|{Fore.RESET}        ',
        f'                        '
        f'                        '
    ],
    "Bearish Closing Marubozu": [
        f'                        ',
        f'            {Fore.RED}║{Fore.RESET}            ',
        f'        {Fore.RED}|███████|{Fore.RESET}        ',
        f'        {Fore.RED}|███████|{Fore.RESET}        ',
        f'        {Fore.RED}|███████|{Fore.RESET}        ',
        f'        {Fore.RED}|███████|{Fore.RESET}        ',
        f'        {Fore.RED}|███████|{Fore.RESET}        ',
        f'        {Fore.RED}|███████|{Fore.RESET}        ',
        f'                        '
    ],

    "Bearish Opening Marubozu": [
        f'                        ',
        f'        {Fore.RED}|███████|{Fore.RESET}        ',
        f'        {Fore.RED}|███████|{Fore.RESET}        ',
        f'        {Fore.RED}|███████|{Fore.RESET}        ',
        f'        {Fore.RED}|███████|{Fore.RESET}        ',
        f'        {Fore.RED}|███████|{Fore.RESET}        ',
        f'        {Fore.RED}|███████|{Fore.RESET}        ',
        f'            {Fore.RED}║{Fore.RESET}            ',
        f'                        '
    ],
    "Long Day Bearish": [
        f'                        ',
        f'            {Fore.RED}║{Fore.RESET}            ',
        f'        {Fore.RED}|███████|{Fore.RESET}        ',
        f'        {Fore.RED}|███████|{Fore.RESET}        ',
        f'        {Fore.RED}|███████|{Fore.RESET}        ',
        f'        {Fore.RED}|███████|{Fore.RESET}        ',
        f'        {Fore.RED}|███████|{Fore.RESET}        ',
        f'        {Fore.RED}|███████|{Fore.RESET}        ',
        f'            {Fore.RED}║{Fore.RESET}            ',
        f'                        '
    ],
    "Long Day Bullish": [
    f'                        ',
    f'            {Fore.GREEN}║{Fore.RESET}            ',
    f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
    f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
    f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
    f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
    f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
    f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
    f'            {Fore.GREEN}║{Fore.RESET}            ',
    f'                        '
    ],

    "Short Day Bearish": [
    f'                        ',
    f'            {Fore.RED}║{Fore.RESET}            ',
    f'            {Fore.RED}║{Fore.RESET}            ',
    f'        {Fore.RED}|███████|{Fore.RESET}        ',
    f'        {Fore.RED}|███████|{Fore.RESET}        ',
    f'        {Fore.RED}|███████|{Fore.RESET}        ',
    f'            {Fore.RED}║{Fore.RESET}            ',
    f'            {Fore.RED}║{Fore.RESET}            ',
    f'                        '
],
    "Short Day Bullish": [
    f'                        ',
    f'            {Fore.GREEN}║{Fore.RESET}            ',
    f'            {Fore.GREEN}║{Fore.RESET}            ',
    f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
    f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
    f'        {Fore.GREEN}|███████|{Fore.RESET}        ',
    f'            {Fore.GREEN}║{Fore.RESET}            ',
    f'            {Fore.GREEN}║{Fore.RESET}            ',
    f'                        '
],

}

def draw_double_patterns():
    for pattern, art in patterns.items():
        print(f'\n{pattern}:\n' + '\n'.join(art))

# Call the function to display double candlestick patterns
if __name__ == '__main__':
    if DEBUG:
        draw_double_patterns()
