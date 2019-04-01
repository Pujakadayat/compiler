"""
Main executable for the compiler.
"""

import sys
import getopt
import logging
import os
from src.util import readFile, writeFile

from src.parser.lrParser import LRParser
import src.lexer.lexer as lexer
from src.parser.grammar import DeclarationList, StatementList, Arguments, Parameters
from src.ir.ir import generateIr
from src.symbolTable.symbolTable import buildSymbolTable, flattenTree
from src.util import CompilerMessage, messages


class Compiler:
    """The main compiler class."""

    def __init__(self, options):
        self.filename = options.get("filename")
        self.grammar = options.get("grammar")
        self.flags = options.get("flags")
        self.output = options.get("output")
        self.input = options.get("input")
        self.tokens = []
        self.parseTree = None
        self.symbolTable = None
        self.ir = None

        # Setup default grammar if none provided
        if self.grammar is None:
            messages.add(
                CompilerMessage("No grammar specified, using default.", "warning")
            )
            self.grammar = "grammars/main_grammar.txt"

        # Setup empty list for flags if none provided
        if self.flags is None:
            self.flags = []

        # Warn if output flag exists but no filename specified
        if "-o" in self.flags and self.output is None:
            messages.add(
                CompilerMessage("No output file specified. Not dumping IR.", "warning")
            )

        # Start a log if verbose flag
        if "-v" in self.flags:
            startLog()

    def tokenize(self):
        """Tokenize the input file."""

        # Read in the file and tokenize
        code = readFile(self.filename)
        self.tokens = lexer.tokenize(code)

        if self.tokens is None:
            raise CompilerMessage("Failed to tokenize the file.")

        messages.add(CompilerMessage("Tokenized the file successfully.", "success"))

        # Print the tokens
        if "-s" in self.flags:
            messages.add(CompilerMessage("Tokens:", "important"))
            for token in self.tokens:
                print(token)

        return self.tokens

    def parse(self):
        """Parse the tokens using our LR Parser."""

        # Cannot parse until we tokenize
        if not self.tokens:
            raise CompilerMessage("Cannot parse without tokenizing first.")

        parser = LRParser()

        # Check if we should force generate the tables
        if "-f" in self.flags:
            parser.loadParseTables(self.grammar, force=True)
        else:
            parser.loadParseTables(self.grammar, force=False)

        # Parse the tokens and save the parse tree
        self.parseTree = parser.parse(self.tokens)

        if self.parseTree is None:
            messages.add(CompilerMessage("Failed to parse the tokens."))
            return None

        messages.add(CompilerMessage("Succesfully parsed the tokens.", "success"))

        # Flatten the parse tree
        flattenTree(self.parseTree, reducer=Arguments)
        flattenTree(self.parseTree, reducer=Parameters)
        flattenTree(self.parseTree, reducer=DeclarationList)
        flattenTree(self.parseTree, reducer=StatementList)

        # Print the parse tree
        if "-p" in self.flags:
            messages.add(CompilerMessage("Parse Tree:", "important"))
            parser.print()

        return self.parseTree

    def buildSymbolTable(self):
        """Build a symbol table from a parse tree."""

        # Cannot build symbol table without parse tree
        if not self.parseTree:
            raise CompilerMessage("Cannot build symbol table without a parse tree.")

        # Save the symbol table
        self.symbolTable = buildSymbolTable(self.parseTree)

        if self.symbolTable is None:
            messages.add(CompilerMessage("Failed to build the symbol table."))
            return None

        messages.add(CompilerMessage("Succesfully built the symbol table.", "success"))

        # Print the symbol table if flag is present
        if "-t" in self.flags:
            messages.add(CompilerMessage("Symbol Table:", "important"))
            self.symbolTable.print()
        return self.symbolTable

    def generateIr(self):
        """Convert a parse tree to the first intermediate representation."""

        # Read in an IR from a file
        if "-i" in self.flags and self.input is not None:
            ir = readFile(self.input)
            self.ir = ir.split("\n")
            return None

        # Cannot convert to IR without parse tree
        if not self.parseTree:
            raise CompilerMessage("Cannot generate an IR without a parse tree.")

        # Cannot convert to IR without symbol table
        if not self.symbolTable:
            raise CompilerMessage("Cannot generate an IR without a symbol table.")

        self.ir = generateIr(self.parseTree)

        if self.ir is None:
            messages.add(CompilerMessage("Failed to generate an IR."))
            return None

        messages.add(CompilerMessage("Succesfully generated an IR.", "success"))

        if "-r" in self.flags:
            messages.add(CompilerMessage("Intermediate Representation:", "important"))
            for i in self.ir:
                print(i)

        if "-o" in self.flags and self.output is not None:
            writeFile(self.output, self.ir)

        return self.ir


def printUsage():
    """Print a usage statement."""

    bold = "\033[1m"
    end = "\033[0m"

    print(f"\n  {bold}Usage{end}:\n")
    print("    python3 main.py [<flags>] filename\n")
    print(f"  {bold}Flags{end}:\n")
    print("     -h, --help                  Output this usage information.")
    print("     -v, --verbose               Generate a log file with debug info.")
    print("     -s, --scanner               Convert a source file into tokens.")
    print("     -p, --parser                Convert tokens into a parse tree.")
    print("     -g, --grammar <filename>    Provide a grammar file to parse with.")
    print(
        "     -t, --table                 Generate a symbol table from the parse tree."
    )
    print(
        "     -f, --force                 Force the Parser to generate a new parse table."
    )
    print("     -r, --representation        Generate an intermediate representation.")
    print("     -i, --input <filename>      Input an IR file and start from there.")
    print("     -o, --output <filename>     Output the IR to a file.")
    print()


def parseArguments():
    """Parse the command line arguments."""

    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            "hvsptfrg:o:i:",
            [
                "help",
                "verbose",
                "scanner",
                "parser",
                "tree",
                "force",
                "representation",
                "grammar=",
                "output=",
                "input=",
            ],
        )
    except getopt.GetoptError as err:
        print(err)
        printUsage()
        sys.exit(2)

    flags = []
    grammar = None
    output = None
    inputFile = None

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            printUsage()
            sys.exit()
        elif opt in ("-s", "--scanner"):
            flags.append("-s")
        elif opt in ("-p", "--parser"):
            flags.append("-p")
        elif opt in ("-v", "--verbose"):
            flags.append("-v")
        elif opt in ("-t", "--tree"):
            flags.append("-t")
        elif opt in ("-f", "--force"):
            flags.append("-f")
        elif opt in ("-o", "--output"):
            output = arg
            flags.append("-o")
        elif opt in ("-i", "--input"):
            inputFile = arg
            flags.append("-i")
        elif opt in ("-r", "--representation"):
            flags.append("-r")
        elif opt in ("-g", "--grammar"):
            grammar = arg

    try:
        filename = args[0]
    except IndexError:
        print("No filename found.")
        printUsage()
        sys.exit()

    return filename, grammar, flags, output, inputFile


def startLog():
    """Initialize a new log file."""

    logs = os.listdir("logs/")
    biggestLog = 0
    for log in logs:
        if len(log.split(".")) == 3:
            if int(log.split(".")[2]) >= biggestLog:
                biggestLog = int(log.split(".")[2]) + 1

    logging.basicConfig(
        filename="logs/compiler.log.%s" % (biggestLog),
        filemode="w",
        level=logging.DEBUG,
    )


def main():
    """Run the compiler from the command line."""

    filename, grammar, flags, output, inputFile = parseArguments()
    options = {
        "filename": filename,
        "grammar": grammar,
        "flags": flags,
        "output": output,
        "input": inputFile,
    }
    compiler = Compiler(options)

    # Define levels for each step of the compiler
    # Run up to max level
    level = 0
    if "-s" in flags:
        level = 1
    if "-p" in flags:
        level = 2
    if "-t" in flags:
        level = 3
    if "-r" in flags:
        level = 4

    try:
        # If not starting from IR
        if "-i" not in flags:
            for i in range(level + 1):
                if i == 1:
                    compiler.tokenize()
                elif i == 2:
                    compiler.parse()
                elif i == 3:
                    compiler.buildSymbolTable()
                elif i == 4:
                    compiler.generateIr()
        else:
            compiler.generateIr()
    except CompilerMessage as err:
        print(err)
        sys.exit(2)
    except KeyboardInterrupt:
        print("")
        messages.add(CompilerMessage("Compiler was interrupted."))
        sys.exit(2)


if __name__ == "__main__":
    main()
