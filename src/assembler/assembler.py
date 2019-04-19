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
        self.table = {}

    def generate(self):
        """Generate the ASM from our intermediate assembly."""

        # Setup .s file
        self.asm.append(".section\t__TEXT,__text,regular,pure_instructions")

        # Loop through every basic block
        for function in self.ir:
            self.setupFunction(function)
            for block in self.ir[function]["blocks"]:
                for instruction in block.instructions:
                    self.parse(instruction)
            self.teardownFunction()

        return self.asm

    def parse(self, ins):
        """Parse an IR instruction."""

        if ins[0] == "ret":
            self.returnStatement(ins)

    def setupFunction(self, name):
        """Instructions that appear at the beginning of every function."""

        self.asm.append(f".globl\t_{name}")
        self.asm.append(f"_{name}:")
        self.asm.append("pushq %rbp")
        self.asm.append("movq %rsp, %rbp")

    def teardownFunction(self):
        """Instructions that appear at the end of every function."""

        self.asm.append("popq %rbp")
        self.asm.append("ret")

    def print(self):
        """Print the ASM instructions."""

        for i in self.asm:
            print(i)

    def write(self, filename):
        """Creates output file for assembly"""

        # Ensure the assembly directory exists
        prefix = "assembly"
        ensureDirectory(prefix)

        with open(f"{prefix}/{filename}", "w") as fileOut:
            fileOut.write("\n".join(self.asm))

    def returnStatement(self, ins):
        """Parse a return statements."""

        if ins[2].isdigit():
            self.asm.append(f"{ins[1]} ${ins[2]}, %eax")
        else:
            self.asm.append(f"{ins[1]} ${self.table[ins[2]]}, %eax")
