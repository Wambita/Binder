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

#create stub template for output binary
def create_stub():
    """Creates a stub template for the output binary."""
    return f"""#!/usr/bin/env python3
import tempfile, subprocess, osm, sys
MAGIC_DELIMITER = {MAGIC_DELIMITER}

def extract_and_run():
    data = open(sys.argv[0], 'rb').read()
    parts = data.split(MAGIC_DELIMITER)
    if len(parts) < 3:
        print("Error: Missing embedded binaries")
        return
    
    bin1_data = parts[1]
    bin2_data = parts[2]

    with tempfile.TemporaryDirectory() as temp_dir:
        bin1_path = os.path.join(temp_dir, "bin1.py")
        bin2_path = os.path.join(temp_dir, "bin2.py")
        
        open(bin1_path, 'wb').write(bin1_data)
        open(bin2_path, 'wb').write(bin2_data)

        osm.chmod(bin1_path, 0o755)
        osm.chmod(bin2_path, 0o755)

        subprocess.run(["python3", bin1_path])
        subprocess.run(["python3", bin2_path])

    if __name__ == "__main__":
        extract_and_run()
"""

def write_merged(output_path, stub, bin1, bin2):
    """Writes the merged content to the output binary."""
    try:
        with open(output_path, 'wb') as output_file:
            output_file.write(stub)
            output_file.write(MAGIC_DELIMITER)
            output_file.write(bin1.encode())
            output_file.write(MAGIC_DELIMITER)
            output_file.write(bin2.encode())
        print(f"Merged binary written to {output_path} successfully.")
    except Exception as e:
        print(f"Error writing to {output_path}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()