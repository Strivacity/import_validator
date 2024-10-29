# import_validator/validator.py

import sys
from .utils import count_commas, print_message, check_pattern
from .constants import NC, RED, PURPLE

def check_comma_consistency(csv_file, expected_commas):
    """Check each line for consistent comma count."""
    print_message(PURPLE, f"\n# Validating comma counts per line ({expected_commas})")

    # open the csv, loop through all lines, count commas
    with open(csv_file, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            comma_count = count_commas(line)
            if comma_count != expected_commas:
                difference = comma_count - expected_commas
                sign = "+" if difference > 0 else ""
                print(f"{RED} {line_number}:{NC} {comma_count} ({sign}{difference})")

def run_validations(csv_file):
    """Runs all validation checks."""
    try:
        # open the csv
        with open(csv_file, 'r') as file:
            lines = file.readlines()

        # check for empty csv
        if not lines:
            print_message(RED, "The CSV file is empty.")
            return

        # run our validations
        first_line_commas = count_commas(lines[0])
        check_comma_consistency(csv_file, first_line_commas)
        check_pattern(csv_file, r'(\s+"?,|,"?\s+)', "commas with surrounding spaces")
        check_pattern(csv_file, r'\d\.\d+E\+\d+', "exponential forms", ignore_case=True)
        check_pattern(csv_file, r'\?', "question marks")
        check_pattern(csv_file, r'(,"?#?n/a"?|"?#?n/a"?,)', "invalid 'n/a' data", ignore_case=True)
        check_pattern(csv_file, r'(,"?null"?|"?null"?,)', "null data", ignore_case=True)

        # we're done
        print_message(PURPLE, "\n# All checks are completed.")

    except FileNotFoundError:
        print_message(RED, f"File {csv_file} not found.")
    except Exception as e:
        print_message(RED, f"An error occurred: {e}")

def main():
    """Main function to execute validation."""
    if len(sys.argv) != 2:
        print_message(RED, "Usage: python3 -m import_validator.validator.py <csv_file>")
        sys.exit(1)

    csv_file = sys.argv[1]
    run_validations(csv_file)

if __name__ == "__main__":
    main()
