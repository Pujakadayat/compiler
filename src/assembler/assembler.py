"""
The main assembler module.
Reads in the IR and generates assembly instructions (x86).
"""

# import logging
# import os
from src.util import ensureDirectory

debug = True


class Assembler:
    """The general assembly class."""

    def __init__(self, ir):
        pass

    def generate(self):
        return "hey"

    def print(self):
        print("assembly here")

    def write(self, filename):
        """Creates output file for assembly"""

        # Ensure the assembly directory exists
        prefix = "assembly"
        ensureDirectory(prefix)

        with open(f"{prefix}/{filename}", "w") as fileOut:
            # TODO: Populate file with assembler output data
            fileOut.write(
                "This is just a test for now.\nWill populate this with data later."
            )
