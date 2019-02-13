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
    filename, flags = parseArguments()

    # Start logging file
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

    # Build LR(1) table
    lrTable = LRTable()
    lrTable.buildTable()
    abstractSyntaxTree = lrTable.parse(tokens)

    # Parse the tokens
    # parser = Parser(tokens)
    # parser.parse()
    print("✨ Completed parsing!")

    # if "-p" in flags:
    #   parser.print()


def printUsage():
    bold = "\033[1m"
    end = "\033[0m"

    print(f"\n  {bold}Usage{end}:\n")
    print("    python3 main.py [<flags>] filename\n")
    print(f"  {bold}Flags{end}:\n")
    print("     -h, --help     Output usage information.")
    print("     -s, --scanner  Convert a source file into tokens.")
    print("     -p, --parser   Convert tokens into a parse tree")
    print()


def parseArguments():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hspf:", ["file="])
    except getopt.GetoptError:
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

    return filename, flags


def readFile(filename):
    try:
        with open(filename) as file:
            return file.read()
    except IOError as err:
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
