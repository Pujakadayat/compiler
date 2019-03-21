"""
Utility functions to be re-used across modules.
"""


def readFile(filename):
    """Read the contents of a file, if it exists."""

    try:
        with open(filename) as file:
            return file.read()
    except IOError:
        raise CompilerMessage(f"Cannot read file: {filename}")


class MessageCollector:
    def __init__(self):
        self.errors = []

    def add(self, error):
        self.errors.append(error)
        print(error)

    def print(self):
        for error in self.errors:
            print(error)


class CompilerMessage(Exception):
    """Custom CompilerMessage exception."""

    def __init__(self, message=None, level="error"):
        self.message = message
        self.level = level

    def __str__(self):
        error = "\x1B[31m"
        warn = "\x1B[33m"
        success = "\x1b[32m"
        important = "\x1b[36m"
        reset = "\x1B[0m"
        bold = "\033[1m"

        if self.level == "warning":
            return f"{bold}{warn}⚠  Warning:{reset} {self.message}"
        if self.level == "message":
            return f"{bold}{success}✔ Success:{reset} {self.message}"
        if self.level == "important":
            return f"{bold}{important}✨ {self.message}{reset}"

        return f"{bold}{error}✖ Error:{reset} {self.message}"


messages = MessageCollector()
