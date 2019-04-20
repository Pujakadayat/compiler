# pylint: disable=eval-used

"""
The main assembler module.
Reads in the IR and generates assembly instructions (x86).
"""

from src.util import ensureDirectory, CompilerMessage


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
        elif ins[0] == "call":
            if ins[3] == "printf":
                self.printStatement(ins)

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
        """
        Lookup a name in our table of memory addresses.
        If it does not exist, we allocate a new spot in memory.
        """

        try:
            return self.table[name]
        except KeyError:
            return self.store(name)

    def store(self, name):
        """Store a variable at a new memory address and record it."""

        if name in self.table:
            raise CompilerMessage(f"Memory address already exists for {name}")

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
        dest = self.get(operand)

        if ins[2] == "!":
            # Not expression i.e. i = !1
            result = eval(f"not {ins[3]}")
            if result is True:
                result = 1
            else:
                result = 0
            self.asm.append(f"movl ${result}, {dest}")
        elif len(ins) > 3:
            # Expression assignment i.e. i = 2 + 2
            lhs = ins[2]
            op = ins[3]
            rhs = ins[4]

            if op == "&&":
                op = "and"
            if op == "||":
                op = "or"

            # If both operators are plain digits, pre-compute it
            if lhs.isdigit() and rhs.isdigit():
                result = int(eval(f"{lhs} {op} {rhs}"))

                self.asm.append(f"movl ${result}, {dest}")
            else:
                # Otherwise there needs to be assembly logic
                self.mathAssignment(dest, lhs, op, rhs)
        else:
            # Single assignment i.e. i = 2
            lhs = ins[2]

            if lhs.isdigit():
                # If assignment of digit, do a literal
                self.asm.append(f"movl ${lhs}, {dest}")
            else:
                # Otherwise change the memory reference of operand
                # to point at the memory address of LHS.
                # This does not generate an ASM instruction, just updates
                # our internal data structure so when we see operand again
                # it uses the correct memory address.
                lhs = self.resolve(lhs)
                self.table[operand] = lhs

    def mathAssignment(self, dest, lhs, op, rhs):
        """Parse various math assignments."""

        if op == "+":
            op = "addl"
        elif op == "-":
            op = "subl"
        elif op == "*":
            op = "mult"
        elif op == "/":
            op = "divl"

        lhs = self.resolve(lhs)
        rhs = self.resolve(rhs)

        self.move(rhs, "%eax")
        self.asm.append(f"{op} {lhs}, %eax")
        self.move("%eax", dest)

    def resolve(self, name):
        """
        Resolves an identifier to either a memory address or a constant.
        Example:
            resolve("2") returns "$2"
            resolve("r1") returns "-8(%rbp)"
        """

        if name.isdigit():
            return f"${name}"

        return self.get(name)

    def move(self, src, dest):
        """ASM instruction to move from src to dest."""

        self.asm.append(f"movl {src}, {dest}")
