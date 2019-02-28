"""
Main executable for the compiler.
"""

import sys
import getopt
import logging
import os
from src.parser.lrParser import LRParser
import src.lexer as lexer
from src.util import readFile


def run(filename, grammar, flags):
    """Run the compiler based on the given command line arguments."""

    # Start logging file
    if "-v" in flags:
        startLog()

    # Read in the program file
    code = readFile(filename)

    # Tokenize the input file
    tokens = lexer.tokenize(code)
    print("✨ Completed scanning!")

    # Handle printing flags
    if "-s" in flags:
        for token in tokens:
            print(token)

    # Load the action and goto tables for parsing
    parser = LRParser()

    if "-f" in flags:
        parser.loadParseTables(grammar, force=True)
    else:
        parser.loadParseTables(grammar, force=False)

    # Parse the program
    isAccepted = parser.parse(tokens)

    if isAccepted:
        print("✨ Completed parsing!")
    else:
        print("✖ The program is not valid.")

    # Print the parseTree
    if "-p" in flags:
        parser.print()

    return isAccepted


def printUsage():
    """Print a usage statement."""

    bold = "\033[1m"
    end = "\033[0m"

    print(f"\n  {bold}Usage{end}:\n")
    print("    python3 main.py [<flags>] [-g grammar] filename\n")
    print(f"  {bold}Flags{end}:\n")
    print("     -h, --help                  Output usage information.")
    print("     -v, --verbose               Generate a log file with debug info.")
    print("     -s, --scanner               Convert a source file into tokens.")
    print("     -p, --parser                Convert tokens into a parse tree.")
    print("     -g, --grammar <filename>    Provide a grammar file to parse with.")
    print(
        "     -f, --force                 Force the Parser to generate a new parse table."
    )
    print()


def parseArguments():
    """Parse the command line arguments."""

    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            "hvspfg:",
            ["help", "verbose", "scanner", "parser", "force", "grammar="],
        )
    except getopt.GetoptError as err:
        print(err)
        printUsage()
        sys.exit(2)

    flags = []
    grammar = "grammars/main_grammar.txt"

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
        elif opt in ("-f", "--force"):
            flags.append("-f")
        elif opt in ("-g", "--grammar"):
            grammar = arg

    try:
        filename = args[0]
    except IndexError:
        print("No filename found.")
        printUsage()
        sys.exit()

    return filename, grammar, flags


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
    filename, grammar, flags = parseArguments()
    run(filename, grammar, flags)


if __name__ == "__main__":
    main()
