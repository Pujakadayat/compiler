import sys
import getopt
import lexer
import logging
import pprint
import os
from parser.parser import Parser
from parser.lrTable import LRTable


def main():
    # Get command line arguments
    filename, grammar, flags = parseArguments()

    # Start logging file
    if "-v" in flags:
        startLog()

    # Read in the program file
    code = readFile(filename)

    # Read in the grammar file
    if grammar:
        grammar = readFile(grammar)

    # Tokenize the input file
    tokens = lexer.tokenize(code)
    print("✨ Completed scanning!")

    # Handle printing flags
    if "-s" in flags:
        for token in tokens:
            print(token)

    # Parse the tokens using an LR(1) table
    lrTable = LRTable(grammar)
    lrTable.buildTable()
    lrTable.parse(tokens)

    print("✨ Completed parsing!")

    # Print the AST
    # if "-p" in flags:
    #   parser.print()


def printUsage():
    bold = "\033[1m"
    end = "\033[0m"

    print(f"\n  {bold}Usage{end}:\n")
    print("    python3 main.py [<flags>] [-g grammar] filename\n")
    print(f"  {bold}Flags{end}:\n")
    print("     -h, --help                  Output usage information.")
    print("     -v, --verbose               Generate a log file with debug info.")
    print("     -s, --scanner               Convert a source file into tokens.")
    print("     -p, --parser                Convert tokens into a parse tree.")
    print("     -f, --file                  The C file to compile.")
    print("     -g, --grammar <filename>    Provide a grammar file to parse with.")
    print()


def parseArguments():
    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            "hvspg:f:",
            ["help", "verbose", "scanner", "parser", "grammar=", "file="],
        )
    except getopt.GetoptError as err:
        print(err)
        printUsage()
        sys.exit(2)

    try:
        filename = args[0]
    except IndexError:
        print("No filename found.")
        printUsage()
        sys.exit()

    flags = []

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
        elif opt in ("-f", "--file"):
            filename = arg
        elif opt in ("-g", "--grammar"):
            grammar = arg

    return filename, grammar, flags


def readFile(filename):
    try:
        with open(filename) as file:
            return file.read()
    except IOError as err:
        print(err)
        print(f"Could not read the file: {filename}")
        sys.exit(2)


def startLog():
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


if __name__ == "__main__":
    sys.exit(main())
