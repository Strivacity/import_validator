# import_validator/utils.py

import re
from .constants import NC, PURPLE, RED

def print_message(color, message):
    """Prints a message in the specified color."""
    print(f"{color}{message}{NC}")

def count_commas(line):
    """Counts the number of commas in a given line."""
    return line.count(',')

def check_pattern(file, pattern, description, ignore_case=False):
    """Generic function to check for a specific regex pattern in each line of the file."""
    flags = re.IGNORECASE if ignore_case else 0
    print_message(PURPLE, f"\n# Checking for {description}...")
    with open(file, 'r') as f:
        for line_number, line in enumerate(f, start=1):
            if re.search(pattern, line, flags):
                print(f"{RED} {line_number}{NC}: {line.strip()}")