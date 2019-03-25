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
    """A collector class that hold compiler messages."""

    def __init__(self):
        self.messages = []

    def add(self, message):
        """Add a new message to the collector, and print it."""

        self.messages.append(message)
        print(message)

    def print(self):
        """Print all the messages in the collector."""

        for message in self.messages:
            print(message)


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


class Spinner:
    """A CLI spinner class."""

    def __init__(self):
        pass

    def start(self):
        """Start the spinner."""

        # TODO: thread work here...
        print("Starting the spinner....")

    def stop(self):
        """Stop the spinner."""

        # TODO: close thread...
        print("Stopping the spinner....")


spinner = Spinner()
messages = MessageCollector()
