class SymbolTable:
    def __init__(self):
        self.table = {}
        self.table["name"] = "global"
        self.table["variables"] = []
        self.current = self.table

    def startScope(self, name):
        # Add the new scope dict
        self.current[name] = {}
        self.current[name]["name"] = name

        # Initialize the dict with a .. and variables entry
        self.current[name][".."] = self.current
        self.current[name]["variables"] = []

        # Update the current pointer
        self.current = self.current[name]

    def declareVariable(self, name):
        # TODO: add type to variable declaration
        # Append the variable to the current scope's variable list
        self.current["variables"].append(name)

    def endScope(self):
        # Go back up one scope
        if ".." in self.current:
            self.current = self.current[".."]

    def find(self, name):
        c = self.current

        # Search the global table first
        if c == self.table:
            if name in c["variables"]:
                return self.table["name"]
            else:
                return None
        else:
            # Search up the tree from our current scope
            # as long as there is a parent
            while ".." in c:
                if name in c["variables"]:
                    return c["name"]
                else:
                    c = c[".."]

        # Not found in any scope, return False
        return None


# Example below on how to use this Symbol Table

"""
C code we will parse:

int i, j;

int main() {
    int i = 0;

    i = j;
}
"""


s = SymbolTable()
s.declareVariable("i")
s.declareVariable("j")
s.startScope("main")
s.declareVariable("i")
ret = s.find("xxx")

print(ret)


# Reductions that will trigger a new scope:

# Functions
# For Statement
# While Statement
# If Statement
