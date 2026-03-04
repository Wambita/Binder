#!/usr/bin/env python3
# Created by: Sheila Fana
# Created on: March 2026
# This program merges the outputs of two binary executables

import sys
import os

MAGIC_DELIMITER = b"\n#--MAGIC_DELIMITER--\n"

def validate_arguments():
    if len(sys.argv) != 5 or sys.argv[3] != "-o":
        print("Usage: ./merge.py <binary1> <binary2> -o <output_binary>")
        sys.exit(1)

    bin1_path, bin2_path, output_path = sys.argv[1], sys.argv[2], sys.argv[4]

    for path in [bin1_path, bin2_path]:
        if not os.path.exists(path):
            print(f"Error: File not found -> {path}")
            sys.exit(1)

    return bin1_path, bin2_path, output_path


def read_binary(file_path):
    try:
        with open(file_path, 'rb') as file:
            print(f"Content of {file_path} read successfully.")
            return file.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        sys.exit(1)


def create_stub():
    """Creates a runtime stub that extracts and runs the embedded binaries."""
    stub_code = """#!/usr/bin/env python3
import tempfile, subprocess, os, sys

MAGIC_DELIMITER = b"\\n#--MAGIC_DELIMITER--\\n"

def extract_and_run():
    try:
        with open(sys.argv[0], 'rb') as f:
            data = f.read()

        parts = data.split(MAGIC_DELIMITER)
        if len(parts) < 3:
            print("Error: Embedded binaries not found.")
            return

        bin1_data = parts[1]
        bin2_data = parts[2]

        with tempfile.TemporaryDirectory() as temp_dir:
            bin1_path = os.path.join(temp_dir, "bin1")
            bin2_path = os.path.join(temp_dir, "bin2")

            with open(bin1_path, 'wb') as f1:
                f1.write(bin1_data)
            with open(bin2_path, 'wb') as f2:
                f2.write(bin2_data)

            os.chmod(bin1_path, 0o755)
            os.chmod(bin2_path, 0o755)

            subprocess.run(["python3", bin1_path])
            subprocess.run(["python3", bin2_path])

    except Exception as e:
        print(f"Runtime Error: {e}")

if __name__ == "__main__":
    extract_and_run()
    os._exit(0)  # ← Critical: prevents Python from parsing appended binary data
"""
    return stub_code.encode("utf-8")


def write_merged(output_path, stub, bin1, bin2):
    try:
        with open(output_path, 'wb') as output_file:
            output_file.write(stub)
            output_file.write(MAGIC_DELIMITER)
            output_file.write(bin1)
            output_file.write(MAGIC_DELIMITER)
            output_file.write(bin2)

        os.chmod(output_path, 0o755)
        print(f"Merged binary written to {output_path} successfully.")
    except Exception as e:
        print(f"Error writing to {output_path}: {e}")
        sys.exit(1)


def main():
    bin1_path, bin2_path, output_path = validate_arguments()

    print(f"Reading binary files: {bin1_path} and {bin2_path} ...")
    bin1_content = read_binary(bin1_path)
    bin2_content = read_binary(bin2_path)

    print("Creating runtime stub...")
    stub = create_stub()

    print("Writing merged binary...")
    write_merged(output_path, stub, bin1_content, bin2_content)


if __name__ == "__main__":
    main()
