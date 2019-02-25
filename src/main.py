import sys
import getopt
import lexer
import logging
import pprint
import os
from parser.lrParser import LRParser


def main():
    # Get command line arguments
    filename, grammar, flags = parseArguments()

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

    parser.parse(tokens)
    print("✨ Completed parsing!")

    # Print the parseTree
    # if "-p" in flags:
    #    parser.print()


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
        elif opt in ("-f", "--file"):
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
