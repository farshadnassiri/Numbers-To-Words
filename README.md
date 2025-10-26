# Numbers to Words Converter

A Python program that converts numerical digits into their written English word equivalents.

## Description

This project provides a command-line tool that takes integer numbers as input and converts them to their English word representation. The program supports numbers from 0 to 1,000,000,000 (one billion).

## Features

- Convert numbers from 0 to 1,000,000,000 to English words
- Interactive command-line interface
- Handles all numbers including:
  - Single digits (0-9)
  - Teens (10-19)
  - Tens (20, 30, 40, etc.)
  - Compound numbers (e.g., 23, 45, 67)
  - Hundreds, thousands, millions, and billions

## Project Structure

```
├── src/
│   ├── main.py          # Main program with interactive loop
│   ├── constants.py     # Number word mappings
│   └── test.ipynb       # Jupyter notebook for testing
└── README.md            # This file
```

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

## Installation

1. Clone the repository or download the project files
2. Navigate to the project directory
3. Make sure Python 3 is installed on your system

## Usage

### Running the Program

```bash
cd src
python main.py
```

### Using the Program

1. Run the program using the command above
2. Enter a number when prompted
3. The program will display the number in words
4. Type 'Q' (case-insensitive) and press Enter to quit
5. Enter any number between 0 and 1,000,000,000

### Examples

```
Please enter your number: 42
Forty Two

Please enter your number: 123
One Hundred Twenty Three

Please enter your number: 5678
Five Thousand Six Hundred Seventy Eight

Please enter your number: 1000000
One Million

Please enter your number: q
Good bye!
```

## How It Works

The program uses a recursive algorithm to convert numbers to words:

1. **Numbers 0-19**: Direct lookup from the UNDER_20 array
2. **Numbers 20-99**: Combines tens and ones (e.g., "Twenty" + "Three")
3. **Numbers 100+**: Recursively breaks down large numbers by finding the largest power of 10 (hundred, thousand, million, billion) and combining it with the remainder

The conversion logic is implemented in the `num_to_word()` function in `main.py`.

## Files

- **main.py**: Contains the main program logic including the `num_to_word()` function and the interactive input loop
- **constants.py**: Defines three dictionaries/arrays:
  - `UNDER_20`: Words for numbers 0-19
  - `TENS`: Words for multiples of 10 (20, 30, etc.)
  - `ABOVE_100`: Words for powers of 10 above 100 (hundred, thousand, million, billion)

## Error Handling

The program handles invalid input gracefully:
- Non-numeric input: Displays "Numbers Only Please!!!"
- Numbers outside the valid range: Displays "Please enter a valid number"
- Empty input: Displays "Numbers Only Please!!!"

## Testing

A Jupyter notebook (`test.ipynb`) is included in the `src` directory for testing various number conversions.

## License

This project is part of a Python learning exercise.

## Author

Created as part of project-based Python exercises.
