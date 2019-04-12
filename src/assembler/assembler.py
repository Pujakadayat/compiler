"""
The main assembler module.
Reads in the IR and generates assembly instructions (x86).
"""

import logging
import os
from src.util import readFile, messages, CompilerMessage

debug = True

".file /src/assembler/filename"


class Assembler:
    """The general assembly class."""

    def __init__(self):
        pass

    def writeFile(self, filename):
        """Creates output file for assembly"""
        with open(filename, "w") as fileOut:
            ## TODO: Populate file with assembler output data
            fileOut.write(
                "This is just a test for now.\nWill populate this with data later."
            )

        print("Done.")
