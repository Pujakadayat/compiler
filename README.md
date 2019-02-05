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

### AST Nodes to Support
## Via: Nora Sandler

- [ ] program = Program(function_declaration)
- [ ] function_declaration = Function(string, statement) #string being the function name
- [ ] statement = Return(exp)
- [ ] exp = Constant(int)

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

- program ::= statement; | program statement;
- statement ::= assign | if | while | print | function
---
- assign ::= intVariable = numericalExpression | boolVariable = boolExpression
- if ::= if boolExpression then program endif | if boolExpression then program else program endif
- while ::= while boolExpression do program endwhile
- print ::= print int | print bool | print char | print string | print intVariable | print boolVariable |
- function ::=
---
- intVariable ::= char string
- boolVariable ::= char string
---
- numericalExpression ::= int | intVariable | s
- s ::= t | s+t | s-t
- t ::= e | txe | t/e
- e ::= p | p^e
- p ::= int | (s)
---
- boolExpression ::= m | boolExpression & m | boolExpression || m
- m ::= o | !m
- o ::= grb | (boolExpression)
- grb ::= bool | boolVariable | numericalExpression == numericalExpression | numericalExpression > numericalExpression | numericalExpression < numericalExpression
---
- string ::= char | int | string char | string int
- char ::= [a - z][A - Z]
- int ::= [0 - 9] | [0 - 9] int
- bool ::= True | False

## Code Style

Using [Black](https://github.com/ambv/black).

## Related

- [SmallerC](https://github.com/alexfru/smallerc)
- [Tiny C Compiler](https://bellard.org/tcc/)
