import sys
import getopt
import lexer
import parser.parser as parser
import logging


def main():
    # Get command line arguments
    filename, flags = parseArguments()

    logging.basicConfig(filename="compiler.log", level=logging.DEBUG)

    # Read in the program file
    code = readFile(filename)

    # Tokenize the input file
    tokens = lexer.tokenize(code)
    print("✨ Completed scanning!")

    # Handle printing flags
    if "-s" in flags:
        print(tokens)

    # Parse the tokens
    parser.parse(tokens)
    print("✨ Completed parsing!")

    if "-p" in flags:
        parser.print()


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


if __name__ == "__main__":
    sys.exit(main())
