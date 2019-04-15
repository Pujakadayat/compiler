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
        self.ir = ir
        self.asm = []

    def generate(self):
        """Generate the ASM from our intermediate assembly."""

        for function in self.ir:
            self.generateFunction(function)
            for block in self.ir[function]["blocks"]:
                for line in block:
                    pass
                    # Parse instruction to ASM

        return self.asm

    def generateFunction(self, name):
        self.asm.append(f"{name}:")
        self.asm.append("pushq %rbp")
        self.asm.append("movq %rsp, %rbp")
        self.asm.append("BLOCK CONTENTS GO HERE...")
        self.asm.append("popq %rbp")
        self.asm.append("ret")

    def print(self):
        for i in self.asm:
            print(i)

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
