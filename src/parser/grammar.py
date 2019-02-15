import tokens as tokenTypes


def printPrefix(level):
    for _ in range(level):
        print("  ", end=" ")
    print("| - ", end=" ")


class Node:
    def __init__(self):
        pass

    def print(self, level=0):
        """
        General node print method.
        First, print the class name, then print all it's children.

        This method is overriden at lower level nodes like NUMCONST.
        """

        printPrefix(level)
        print(self.__class__.__name__)

        for child in self.children:
            child.print(level + 1)


class Program(Node):
    def __init__(self, *children):
        self.children = children


class FunctionDeclaration(Node):
    def __init__(self, *children):
        self.children = children


class TypeSpecifier(Node):
    def __init__(self, value):
        self.value = value

    def print(self, level):
        printPrefix(level)
        print(f"{self.__class__.__name__}: {self.value}")


class ReturnStatement(Node):
    def __init__(self, *children):
        self.children = children


class NUMCONST(Node):
    def __init__(self, value):
        self.value = value

    def print(self, level):
        printPrefix(level)
        print(f"{self.__class__.__name__}: {self.value}")


class IDENTIFIER(Node):
    def __init__(self, value):
        self.value = value

    def print(self, level):
        printPrefix(level)
        print(f"{self.__class__.__name__}: {self.value}")
