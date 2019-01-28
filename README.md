# Compiler in Python: Design Documents

Group Members: Charles Hermann, Izeah Olguin, Paco Coursey

## Quickstart

Clone the repository:

```bash
$ git clone https://github.com/pacocoursey/compiler.git
```

## Usage

The compiler requires Python or later.

### `character_count`

Ensure that a `.txt` file is within working directory. Run using:

```bash
$ python3 character_count.py FILENAME
```

## Implementation Overview

### Required Features

Features required in our implementation.

- [ ] Functions
- [ ] Return
- [ ] Break
- [ ] Variables
- [ ] Arithmetic (+, -, *,)
- [ ] Assignment
- [ ] Boolean Expressions
- [ ] Goto
- [ ] If
- [ ] While
- [ ] Unary Operators
- [ ] Integers (default, signed, syslen)

### Extra Features

Extra features for bonus points.

- [ ] `char`, `float`
- [ ] For
- [ ] Switch
- [ ] Binary Operators (&, |, ^)
- [ ] Assignment Helpers (+=, -=, *=, /=, ++, --)

### Out of Bound Features

Extremely extra features.

- Pointers
- Arrays
- Compiler Preprocessing (macros, #include)
- Struct
- Enum
- Library Calls
- Casting
- Promotion
- Strings
- Type Specs

### Proposed Grammar

- PROGRAM ::= STATEMENT; | PROGRAM STATEMENT;
- STATEMENT ::= ASSIGN | IF | WHILE | PRINT

- ASSIGN ::= NUMERICAL_VARIABLE = NUMERICAL_EXPRESSION | BOOLEAN_VARIABLE = BOOLEAN_EXPRESSION
- IF ::= if BOOLEAN_EXPRESSION then PROGRAM endif | if BOOLEAN_EXPRESSION then PROGRAM else PROGRAM endif
- WHILE ::= while BOOLEAN_EXPRESSION do PROGRAM endwhile
- PRINT ::= print NUM | print bool | print NUMERICAL_VARIABLE | print BOOLEAN_VARIABLE | print STRING

- NUMERICAL_VARIABLE ::= CHAR STRING
- BOOLEAN_VARIABLE ::= CHAR STRING

- NUMERICAL_EXPRESSION ::= NUM | NUMERICAL_VARIABLE | S
- S ::= T | S+T | S-T
- T ::= E | TxE | T/E
- E ::= P | P^E
- P ::= NUM | (S)

- BOOLEAN_EXPRESSION ::= M | BOOLEAN_EXPRESSION & M | BOOLEAN_EXPRESSION || M
- M ::= O | !M
- O ::= GRB | (BE)
- GRB ::= BOOL | BOOLEAN_VARIABLE | NUMERICAL_EXPRESSION == NUMERICAL_EXPRESSION | NUMERICAL_EXPRESSION > NUMERICAL_EXPRESSION | NUMERICAL_EXPRESSION < NUMERICAL_EXPRESSION 

- STRING ::= CHAR | NUM | STRING CHAR | STRING NUM
- CHAR ::= [a - z][A - Z]
- NUM ::= [0 - 9] | [0 - 9] NUM
- BOOL ::= True | False

## Code Style

Using [Black](https://github.com/ambv/black).

## Related

- [SmallerC](https://github.com/alexfru/smallerc)
- [Tiny C Compiler](https://bellard.org/tcc/)
