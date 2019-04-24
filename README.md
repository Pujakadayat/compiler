# Compiler in Python: Design Document

Group Members: Charles Hermann, Izeah Olguin, Paco Coursey

Last Updated: 03/31/2019

# Quickstart

Clone the repository:

```bash
$ git clone https://github.com/pacocoursey/compiler.git
```

Install the dependencies using [pip3](https://pypi.org/project/pip/):

```bash
$ make install
```

# Overview

Our python compiler currently meets the standards expected of the second deliverable.

Our scanner reads in a file as a string of characters and produces a list of labeled tokens. These tokens are acquired by the parser and are used to produce a parse tree. The parse tree is used to construct a symbol table. Then the parse tree and symbol table are used to generate an intermediate representation of the program.

The parse tree is created using action and goto tables generated from our grammar rules. We use an LR(1) shift reduce parser. We then flatten out the recursive grammar rules of the parse tree using a recursive Depth First Traversal to remove redundant tree nodes.

The symbol table is created by scanning the parse tree in Depth First order and creating new scopes for each function declaration. We error check for undefined identifiers and duplicate declarations here.

Our intermediate representation is also generated by a Depth First traversal of the parse tree. We call an IR method for each node of the tree and save the result as a list of strings. We use three-address code in combination with temporary variables to represent the program.

As a group, we have met numerous times to discuss our design, implementation and overall expectations of our compiler, which has lead to overcoming numerous amounts of errors and feats against our design endeavors.

# Usage

Our compiler uses Python 3.

### Character Count

This program returns the number of characters found in a given file. Run using:

```bash
$ python3 -m src.character_count FILENAME
```

## Compiler Flags

### `-h` or `--help`

Print usage information.

### `-v` or `--verbose`

Logs additional output to a file in `/logs`.

### `-f` or `--force`

Forcefully generate new action and goto tables from the specified grammar rules and save them in `/tables`.

### `-g` or `--grammar`

Specify a grammar to use. Defaults to `/grammars/main_grammar.txt`. Run using:

```bash
$ python3 -m src.main -g GRAMMAR_FILENAME FILENAME
# or
$ python3 -m src.main --grammar GRAMMAR_FILENAME FILENAME
```

### `-s` or `--scan`

Tokenizes a C program and returns a list of the known tokens. Run using:

```bash
$ python3 -m src.main -s FILENAME
# or
$ python3 -m src.main --scan FILENAME
```

### `-p` or `--parse`

Converts a list of tokens generated by the scanner and constructs an abstract representation of the program using a pre-defined C grammar. Run using:

```bash
$ python3 -m src.main -p FILENAME
# or
$ python3 -m src.main --parse FILENAME
```

### `-t` or `--table`

Generate a symbol table using the parse tree to keep a list of scopes and defined variables. Run using:

```bash
$ python3 src/main -t FILENAME
# or
$ python3 src/main --table FILENAME
```

### `-r` or `--ir`

Generate an Intermediate Representation. Run using:

```bash
$ python3 -m src.main -r FILENAME
# or
$ python3 -m src.main --ir FILENAME
```

### `-i` or `--input`

Read in an IR instead of source file. Run using:

```bash
$ python3 -m src.main -i INPUT_IR
# or
$ python3 -m src.main --input INPUT_IR
```

### `-o` or `--output`

Write out the IR to a file. Run using:

```bash
$ python3 -m src.main -r -o OUTPUT_FILENAME FILENAME
# or
$ python3 -m src.main --ir --output OUTPUT_FILENAME FILENAME
```

### `-a` or `--asm`

Generate assembly instructions from the IR. Run using:

```bash
$ python3 -m src.main -a FILENAME
# or
$ python3 -m src.main --asm FILENAME
```

### `-n` or `--asmOutput`

Write out the assembly to a file. Run using:

```bash
$ python3 -m src.main -a -n OUTPUT_FILENAME FILENAME
# or
$ python3 -m src.main --asm --asmOutput OUTPUT_FILENAME FILENAME
```

# Design Discussion

## Scanner Implementation

Our scanner parses characters in a 'chunk', with a start an and end counter. We iterate through the chunk to match our tokens in the following order: Symbols, Operators, Keywords, Identifiers and Numbers.

We are not focused on speed, which is why we opted not to use regular expressions. This gives us more logical control over what tokens we recognize, and it is easier to handle edge cases like multi-line comments.

## Parser Implementation

Our parser uses action and goto tables generated from the rules in `grammars/main_grammar.txt`. Because generating the tables takes so long, after the first generation they are saved in JSON format in the `tables/` directory for future compiler executions. The parser outputs a parse tree consisting of instances of custom node classes defined in `grammar.py`. The parse tree nodes are highly abstracted and do not include unimportant tokens like brackets or parentheses.

After the initial creating of the parse tree, it is "flattened" by un-nesting recursive grammar nodes. This makes it easier to generate the symbol table and removes useless duplicate nodes from the tree.

## Symbol Table Implementation

Our symbol table uses the parse tree to create a new scope for each function declaration. We save each variable declaration inside the appropriate scope, including a global scope. While generating the symbol table we also check for duplicate variable, function declaration and undefined identifiers.

## IR Implementation

The intermediate representation is generated by visiting each node of the parse tree in Depth First order and calling an IR method on each node. These IR methods are defined differently for each node in `grammar.py`. The IR methods currently return strings, and are saved in a simple list.

We use three-address code and intermediate variables to assist with our IR generation. The intermediate variables are uniquely generated so that we can avoid unclear assignments.

Our compiler can skip all of the above steps and start from an already generated IR file by using the `-i` or `--input` flags. You can dump the intermediate representation of a program to a file using the `-o` or `--output` flags.

## Design Benefits

- Few files, things can be modified quickly
- Design and hierarchy is well established
- Good separation of concepts into modularized files
- Able to iterate quickly on all aspects of the compiler

## Grammar Specification

|    Required Features   | Scanner | Parser | IR | ASM |
|------------------------|:-------:|:------:|:--:|:---:|
|       Identifiers      |    ✔️    |    ✔️   |  ✔️ |  ✔️  |
|        Variables       |    ✔️    |    ✔️   |  ✔️ |  ✔️  |
|        Functions       |    ✔️    |    ✔️   |  ✔️ |  ✔️  |
|        Keywords        |    ✔️    |    ✔️   |  ✔️ |  ✔️  |
| Arithmetic Expressions |    ✔️    |    ✔️   |  ✔️ |  ✔️  |
|       Assignment       |    ✔️    |    ✔️   |  ✔️ |  ✔️  |
|   Boolean Expressions  |    ✔️    |    ✔️   |  ✔️ |  ✔️  |
|     Goto Statements    |    ✔️    |    ✔️   |  ✔️ |  ✔️  |
|  If/Else Control Flow  |    ✔️    |    ✔️   |  ✔️ |  ✔️  |
|     Unary Operators    |    ✔️    |    ✔️   |  ✔️ |  ✔️  |
|    Return Statements   |    ✔️    |    ✔️   |  ✔️ |  ✔️  |
|    Break Statements    |    ✔️    |    ✔️   |  ✔️ |  ✔️  |
|       While Loops      |    ✔️    |    ✔️   |  ✔️ |  ✔️  |

|     Optional Features     | Scanner | Parser | IR | ASM |
|---------------------------|:-------:|:------:|:--:|:---:|
| Types other than Integers |    ✔️    |    ✔️   |  ✔️ |     |
|   ++, --, -=, +=, *=, /=  |    ✔️    |    ✔️   |  ✔️ |  ✔️  |
|         For Loops         |    ✔️    |    ✔️   |  ✔️ |  ✔️  |
|      Binary Operators     |    ✔️    |    ✔️   |  ✔️ |     |
|     Switch Statements     |         |        |    |     |

| Extremely Extra Features | Scanner | Parser | IR | ASM |
|--------------------------|:-------:|:------:|:--:|:---:|
|         Pointers         |         |        |    |     |
|          Arrays          |         |        |    |     |
|          Strings         |         |        |    |     |
|  Preprocessor Statements |         |        |    |     |
|          Struct          |         |        |    |     |
|           Enum           |         |        |    |     |
|          Casting         |         |        |    |     |
|      Type Promotion      |         |        |    |     |
|        Type Specs        |         |        |    |     |

## Code Style

Formatted using [Black](https://github.com/ambv/black). Linted using [PyLint](https://www.pylint.org/).

## Related

- [SmallerC](https://github.com/alexfru/smallerc)
- [Tiny C Compiler](https://bellard.org/tcc/)
