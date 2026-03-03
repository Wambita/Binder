#!/usr/bin/env python3
# Created by: Sheila Fana
# Created on: March 2026
# This program merges the outputs of two binary executables

import sys

def main():
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 5 or sys.argv[3] != "-o":
        print("Usage: ./merge.py bin1 bin2 -o output_binary")
        sys.exit(1)

    print("Arguments validated successfully.")

if __name__ == "__main__":
    main()