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
        # Append the variable to the current scope's variable list
        self.current["variables"].append(name)

    def endScope(self):
        # Go back up one scope
        self.current = self.current[".."]

    def find(self, name):
        c = self.current

        # Search the global table first
        if c == self.table:
            if name in c["variables"]:
                return self.table["name"]
            else:
                return False
        else:
            # Search up the tree from our current scope
            # as long as there is a parent
            while ".." in c:
                if name in c["variables"]:
                    return c["name"]
                else:
                    c = c[".."]

        # Not found in any scope, return False
        return False


# Example below on how to use this Symbol Table

"""
var = "zzz"

s = SymbolTable()
s.declareVariable("x")
s.declareVariable("y")
s.declareVariable("z")
s.startScope("foo")
s.declareVariable("x")
out = s.find(var)
if out is not False:
    print(f"Found the variable {var} in scope: {out}.")
else:
    print(f"The variable {var} was not found in any scope.")
s.endScope()
"""
