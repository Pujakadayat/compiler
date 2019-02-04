import sys


def usage():
    print("\n  Usage:")
    print("    python character_count.py [filename]\n")


# Ensure filename is passed as command line argument
if len(sys.argv) < 2:
    print("Filename not specified.")
    usage()
    sys.exit(-1)

f_name = sys.argv[1]

try:
    file_in = open(f_name, "r")
    num_chars = 0

    for line in file_in:
        word_list = line.split()

        # Produces length of each word and appends to sum
        num_chars += sum(len(word) for word in word_list)

    print(str(num_chars) + " Characters")
except FileNotFoundError:
    print(f"The file {f_name} cannot be opened.")
