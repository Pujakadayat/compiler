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

- ASSIGN ::= NUMERICALVARIABLE = NUMERICALEXPRESSION | BOOLEANVARIABLE = BOOLEANEXPRESSION
- IF ::= if BOOLEANEXPRESSION then PROGRAM endif | if BOOLEANEXPRESSION then PROGRAM else PROGRAM endif
- WHILE ::= while BOOLEANEXPRESSION do PROGRAM endwhile
- PRINT ::= print num | print bool | print NUMERICALVARIABLE | print BOOLEANVARIABLE | print STRING

- NV ::= char STRING
- BV ::= char STRING

- NE ::= num | NV | S
- S ::= T | S+T | S-T
- T ::= E | TxE | T/E
- E ::= P | P^E
- P ::= num | (S)

- BE ::= M | BE & M | BE || M
- M ::= O | !M
- O ::= GRB | (BE)
- GRB ::= bool | BV | NE == NE | NE > NE | NE < NE 

- STRING ::= char | num | STRING char | STRING num
- char ::= [a - z][A - Z]
- num ::= [0 - 9] | [0 - 9] num

## Code Style

Using [Black](https://github.com/ambv/black).

## Related

- [SmallerC](https://github.com/alexfru/smallerc)
- [Tiny C Compiler](https://bellard.org/tcc/)
