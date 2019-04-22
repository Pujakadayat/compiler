# pylint: disable=eval-used, missing-docstring

"""
The main assembler module.
Reads in the IR and generates assembly instructions (x86).
"""

import re
from src.util import ensureDirectory, CompilerMessage

order = ["%r8d", "%r9d", "%r10d", "%r11d", "%r12d", "%r13d", "%r14d", "%r15d"]


def isNumber(s):
    if re.match(r"^-?[0-9]+$", s):
        return True

    return False


class Assembler:
    """The general assembly class."""

    def __init__(self, ir):
        self.ir = ir
        self.asm = []

    def generate(self):
        """Generate the ASM from our intermediate assembly."""

        # Setup .s file
        self.asm.append(".section\t__TEXT,__text,regular,pure_instructions")

        # Loop through every basic block
        for function in self.ir:
            f = Function(
                function,
                self.ir[function]["blocks"],
                self.ir[function]["arguments"],
                self.ir[function]["declarations"],
            )
            self.asm.extend(f.asm)

        return self.asm

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


class Function:
    def __init__(self, name, blocks, arguments, declarations):
        self.name = name
        self.blocks = blocks
        self.arguments = arguments
        self.memory = 0
        self.table = {}
        self.asm = []

        if declarations:
            self.align = declarations * 4
        else:
            self.align = None

        self.setup()
        for block in blocks:
            for instruction in block.instructions:
                self.parse(instruction)
        self.teardown()

    def parse(self, ins):
        """Parse an IR instruction."""

        op = ins[0]

        if op == "label":
            self.label(ins)
        if op == "ret":
            self.returnStatement(ins)
        elif op == "goto":
            self.goto(ins)
        elif op == "if":
            self.ifStatement(ins)
        elif op == "call":
            self.call(ins)
        elif ins[1] == "=":
            self.assignment(ins)

    def setup(self):
        """Instructions that appear at the beginning of every function."""

        self.asm.append(f".globl\t_{self.name}")
        self.asm.append(f"_{self.name}:")
        self.asm.append("pushq %rbp")
        self.asm.append("movq %rsp, %rbp")

        # Add space on the stack according to the number of arguments
        if self.align:
            self.asm.append(f"subq ${self.align}, %rsp")

        if self.arguments:
            self.comment("Moving parameters out of registers")
            for i, arg in enumerate(self.arguments):
                memory = self.store(arg)
                self.move(order[i], memory)

    def teardown(self):
        """Instructions that appear at the end of every function."""

        # If there was no return statement in the function
        # we automatically append one.
        if self.asm[-1] != "retq":
            if self.align:
                self.asm.append(f"addq ${self.align}, %rsp")
            self.asm.append("popq %rbp")
            self.asm.append("retq")

        print(self.table)

    def print(self):
        """Print the ASM instructions."""

        for i in self.asm:
            print(i)

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

    def resolve(self, name):
        """
        Resolves an identifier to either a memory address or a constant.
        Example:
            resolve("2") returns "$2"
            resolve("r1") returns "-8(%rbp)"
        """

        if isNumber(name):
            return f"${name}"

        return self.get(name)

    def move(self, src, dest):
        """ASM instruction to move from src to dest."""

        if isinstance(src, int) or isNumber(src):
            self.asm.append(f"movl ${src}, {dest}")
        else:
            self.asm.append(f"movl {src}, {dest}")

    def comment(self, c):
        """Add a comment to the ASM instructions."""

        self.asm.append(f"\t\t # {c}")

    # Parsing for specific types of instructions

    def returnStatement(self, ins):
        self.comment(f"Return {ins[1]}")

        if isNumber(ins[1]):
            # If returning a digit, do a literal
            self.move(ins[1], "%eax")
        else:
            # Otherwise look up the memory address
            self.move(self.get(ins[1]), "%eax")

        if self.align:
            self.asm.append(f"addq ${self.align}, %rsp")

        self.asm.append("popq %rbp")
        self.asm.append("retq")

    def assignment(self, ins):
        operand = ins[0]
        dest = self.get(operand)

        if ins[2] == "!":
            # Not expression i.e. i = !1
            result = eval(f"not {ins[3]}")
            if result is True:
                result = 1
            else:
                result = 0

            self.move(result, dest)
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
            if isNumber(lhs) and isNumber(rhs):
                try:
                    result = int(eval(f"{lhs} {op} {rhs}"))
                except ZeroDivisionError:
                    raise CompilerMessage(f"Cannot divide by zero: {lhs} {op} {rhs}")
                self.move(result, dest)
            else:
                # Otherwise there needs to be assembly logic
                self.mathAssignment(dest, lhs, op, rhs)
        else:
            # Single assignment i.e. i = 2
            lhs = ins[2]

            if isNumber(lhs):
                # If assignment of digit, do a literal
                self.move(lhs, dest)
            else:
                # Move the value of LHS into the destination
                self.comment(f"Moving {lhs} into {operand}")
                dest = self.resolve(operand)
                lhs = self.resolve(lhs)
                self.move(lhs, "%eax")
                self.move("%eax", dest)

    def mathAssignment(self, dest, lhs, op, rhs):
        # Handle comparison assignments separately
        if op in [">=", "<=", ">", "<", "!=", "=="]:
            self.comparisonAssignment(dest, lhs, op, rhs)
            return

        if op == "%":
            self.modulo(dest, lhs, rhs)
            return

        if op == "/":
            self.division(dest, lhs, rhs)
            return

        if op == "+":
            op = "addl"
        elif op == "-":
            op = "subl"
        elif op == "*":
            op = "imull"

        lhs = self.resolve(lhs)
        rhs = self.resolve(rhs)

        self.move(lhs, "%eax")
        self.asm.append(f"{op} {rhs}, %eax")
        self.move("%eax", dest)

    def modulo(self, dest, lhs, rhs):
        lhs = self.resolve(lhs)
        rhs = self.resolve(rhs)

        self.comment(f"Modulo expression {lhs} % {rhs}")

        self.move(lhs, "%eax")
        self.asm.append("cltd")
        self.move(rhs, "%ecx")
        self.asm.append("idivl %ecx")
        self.move("%edx", dest)

    def division(self, dest, lhs, rhs):
        lhs = self.resolve(lhs)
        rhs = self.resolve(rhs)

        self.comment(f"Division expression {lhs} / {rhs}")

        self.move(lhs, "%eax")
        self.asm.append("cltd")
        self.asm.append(f"idivl {rhs}")
        self.move("%eax", dest)

    def label(self, ins):
        self.asm.append(f"{ins[1]}:")

    def goto(self, ins):
        self.asm.append(f"jmp {ins[1]}")

    def ifStatement(self, ins):
        condition = self.resolve(ins[1])
        elseLabel = ins[6]

        # If the condition is false, we jump to the elseBody
        # Otherwise, we automatically continue to the ifBody
        # as it is the next assembly instruction.
        self.asm.append(f"cmpl $0, {condition}")
        self.asm.append(f"je {elseLabel}")

    def comparisonAssignment(self, dest, lhs, op, rhs):
        lhs = self.resolve(lhs)
        rhs = self.resolve(rhs)

        if op == "==":
            op = "sete"
        elif op == "!=":
            op = "setne"
        elif op == ">":
            op = "setg"
        elif op == "<":
            op = "setl"
        elif op == ">=":
            op = "setge"
        elif op == "<=":
            op = "setle"

        if not isNumber(lhs) and not isNumber(rhs):
            # If both comparators are memory addresses
            # one of them must be moved into %eax
            self.move(lhs, "%eax")
            lhs = "%eax"

        if isNumber(rhs):
            # RHS is a number, must be the LHS of the comparison
            # i.e. the instruction `cmpl -4(%rbp), $1` is invalid
            # it must be `cmpl $1, -4(%rbp)`
            self.asm.append(f"cmpl {lhs}, {rhs}")
        else:
            self.asm.append(f"cmpl {rhs}, {lhs}")

        self.asm.append(f"{op} %cl")
        self.asm.append("andb $1, %cl")
        self.asm.append("movzbl %cl, %edx")
        self.asm.append(f"movl %edx, {dest}")

    def call(self, ins):
        dest = ins[1]
        name = ins[3]
        arguments = ins[4]

        self.comment("Moving arguments into registers")
        for index, argument in enumerate(arguments):
            self.move(self.resolve(argument), order[index])

        self.asm.append(f"callq _{name}")

        self.comment("Saving the return value")
        self.move("%eax", self.resolve(dest))
