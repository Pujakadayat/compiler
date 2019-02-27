"""
Utility functions to be re-used across modules.
"""

def readFile(filename):
    """Read the contents of a file, if it exists."""

    try:
        with open(filename) as file:
            return file.read()
    except IOError as err:
        print(err)
        print(f"Could not read the file: {filename}")
        sys.exit(2)
