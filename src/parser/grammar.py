import tokens as tokenTypes


def parseToken(desc, content = "", children = []):
    if desc == "program":
        return Program(children)
    elif desc == "functionDeclaration":
        return FunctionDeclaration(children)
    elif desc == "returnStatement":
        return ReturnStatement(children)
    elif desc == "typeSpecifier":
        return TypeSpecifier(content)
    elif desc == "ID":
        return Identifier(content)
    elif desc == "constNum":
        return ConstNum(content)
    else:
        return GeneralNode(content, children)

def printPrefix(level):
    for _ in range(level):
        print("  ", end=" ")
    print("| - ", end=" ")


class Node:
    def __init__(self):
        pass

    def __str__(self):
        return self.__class__.__name__

    def print(self, level=0):
        """
        General node print method.
        First, print the class name, then print all it's children.

        This method is overriden at lower level nodes like NUMCONST.
        """

        printPrefix(level)
        print(self.__class__.__name__)

        for child in self.children[0]:
            child.print(level+1)


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

    def print(self, level):
        printPrefix(level)
        print(f"{self.__class__.__name__}")
        for child in self.children[0]:
            child.print(level+1)


class ConstNum(Node):
    def __init__(self, value):
        self.value = value

    def print(self, level):
        printPrefix(level)
        print(f"{self.__class__.__name__}: {self.value}")


class Identifier(Node):
    def __init__(self, value):
        self.value = value

    def print(self, level):
        printPrefix(level)
        print(f"{self.__class__.__name__}: {self.value}")


class GeneralNode(Node):
    def __init__(self, value, children = []):
        self.value = value
        self.children = children

    def print(self, level):
        #if len(self.children) == 0:
        #    printPrefix(level)
        #    print(self.value)
        #else:
        for child in self.children:
            child.print(level)
