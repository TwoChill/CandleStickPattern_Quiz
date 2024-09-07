# CandleStickPattern_Quiz

A Python-based quiz application designed to help users learn and identify various candlestick patterns used in technical analysis for trading. This script dynamically imports candlestick pattern files, presents a quiz to the user, and provides explanations and trading actions based on user responses.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Pattern Files](#pattern-files)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Interactive Quiz**: Identify various candlestick patterns through a series of questions.
- **Dynamic Imports**: Automatically loads pattern files from the directory to keep the quiz up to date.
- **Explanations and Insights**: Provides detailed explanations and trading actions for each pattern.
- **Customizable**: Easily add new pattern files to expand the quiz.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/TwoChill/CandleStickPattern_Quiz.git
    cd CandleStickPattern_Quiz
    ```

2. **Install Required Packages**:
    Ensure you have the necessary packages installed. You can install them using pip:
    ```bash
    pip install colorama termcolor
    ```

3. **Run the Script**:
    Start the quiz by running:
    ```bash
    python main.py
    ```

## Usage

- Upon running the script, you will be prompted to select candlestick pattern files to include in the quiz.
- Answer the multiple-choice questions to identify different candlestick patterns.
- Receive explanations and trading actions based on your responses.

## Pattern Files

- `single_patterns.py`: Defines individual candlestick patterns such as Doji, Bullish Marubozu, Bearish Marubozu, etc.
- You can add more pattern files following the format used in `single_patterns.py` to expand the quiz.

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m "Add some feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to reach out for any questions or suggestions! Happy coding!
