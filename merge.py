#!/usr/bin/env python3
# Created by: Sheila Fana
# Created on: March 2026
# This program merges the outputs of two binary executables

import sys

def main():
    """Main function to merge the outputs of two binary executables."""
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 5 or sys.argv[3] != "-o":
        print("Usage: ./merge.py bin1 bin2 -o output_binary")
        sys.exit(1)
    bin1_data = read_binary(sys.argv[1])
    bin2_data = read_binary(sys.argv[2])
    print("Arguments validated successfully.")

    # Merge the two binary contents with a delimiter
    MAGIC_DELIMITER = b"---BINARY_DELIMITER---"


def read_binary(file_path):
    """Reads the content of a binary file and returns it as a string."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"Content of {file_path} read successfully.")
            return content
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        sys.exit(1)




if __name__ == "__main__":
    main()