import sys
import getopt
import lexer
import parser


def main():
    # Get command line arguments
    filename, flags = parseArguments()

    # Read in the file
    code = readFile(filename)

    # If neither of the flags passed, show usage and exit
    if "-s" not in flags and "-p" not in flags:
        printUsage()
        sys.exit()

    # If scanner flag, tokenize the file
    if "-s" in flags:
        lexer.tokenize(code)

    ##trying to call Parser
    parse = parser.Parser(tokens)
    parse.parse()    

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
