"""
The main assembler module.
Reads in the IR and generates assembly instructions (x86).
"""

from src.util import ensureDirectory


class Assembler:
    """The general assembly class."""

    def __init__(self, ir):
        self.ir = ir
        self.asm = []
        self.table = {}
        self.memory = 0

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
        elif ins[1] == "=":
            self.assignment(ins)

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

    def get(self, name):
        """Lookup a name in our table of memory addresses."""

        try:
            return self.table[name]
        except KeyError:
            return None

    def store(self, name):
        """Store a variable at a new memory address and record it."""

        # Increment memory by 4 bytes
        self.memory += 4

        value = f"-{self.memory}(%rbp)"

        # Save at -$x(%rbp)
        self.table[name] = value

        return value

    def returnStatement(self, ins):
        """Parse a return statements."""

        if ins[1].isdigit():
            # If returning a digit, do a literal
            self.asm.append(f"movl ${ins[1]}, %eax")
        else:
            # Otherwise look up the memory address
            self.asm.append(f"movl {self.get(ins[1])}, %eax")

    def assignment(self, ins):
        """Parse various assignment statements."""

        operand = ins[0]
        loc = self.get(operand)
        if loc is None:
            loc = self.store(operand)

        if len(ins) > 3:
            # Expression assignment i.e. i = 2 + 2
            lhs = ins[2]
            op = ins[3]
            rhs = ins[4]

            # If both operators are plain digits, pre-compute it
            if lhs.isdigit() and rhs.isdigit():
                # pylint: disable=eval-used
                result = eval(f"{lhs} {op} {rhs}")
                # pylint: enable=eval-used

                self.asm.append(f"movl ${result}, {loc}")
            else:
                # Otherwise there needs to be assembly logic
                self.mathAssignment(ins)
        else:
            # Single assignment i.e. i = 2
            lhs = ins[2]

            if lhs.isdigit():
                # If assignment of digit, do a literal
                self.asm.append(f"movl ${lhs}, {loc}")
            else:
                # Otherwise change the memory reference
                self.table[lhs] = loc

    def mathAssignment(self, ins):
        """Parse various math assignments."""

        lhs = ins[2]
        op = ins[3]
        rhs = ins[4]

        if op == "+":
            op = "addl"
        elif op == "-":
            op = "subl"

        # rhs is the thing being added to lhs
        dest = self.get(lhs)

        if isinstance(rhs, int) or rhs.isdigit():
            # Move dest to %eax
            self.move(dest, "%eax")

            # Add src to %eax
            self.asm.append(f"{op} ${rhs}, %eax")

            # Move %eax to dest
            self.move("%eax", dest)
        else:
            src = self.get(rhs)

            # Move dest to %eax
            self.move(dest, "%eax")

            # Add src to %eax
            self.asm.append(f"{op} {src}, %eax")

            # Move %eax back to dest
            self.move("%eax", dest)

    def move(self, src, dest):
        """ASM instruction to move from src to dest."""

        self.asm.append(f"movl {src}, {dest}")
