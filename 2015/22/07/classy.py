
# emulates little Bobby table's circut toy

# generic nodes need to know their parents
class node(object):
    def __init__(self):
        self.parents = []

    def addParent(self, parent):
        self.parents.append(parent)

    def getParents(self):
        return self.parents

    def getValue(self) -> int:
        return None

# specific node type: value
# has a value 
class value(node):
    def __init__(self, val):
        super().__init__()
        self.val = val

    def getValue(self) -> int:
        return self.val

# specific node type: address
# has a name
# 1 parent
class address(node):
    def __init__(self, name):
        super().__init__()
        # specific stuff
        self.name  = name

    # inherited 
    def addParent(self, parent):
        super().addParent(parent)
    
    def getValue(self) -> int:
        parents = super().getParents()
        voltage = parents[0].getValue()
        if voltage < 0: # voltage wraps
            voltage += 65535 + 1
        return voltage

# specific node type: opperation
# knows what opperation it is
# 1-2 parents

# possible opperations:
#   AND    - bitwise and
#   LSHIFT - left-shift
#   RSHIFT - right-shift
#   NOT    - bitwise complement
#   OR     - bitwise or
class opperation(node):
    def __init__(self, oppr):
        super().__init__()
        self.oppr = oppr

    # get nodes parents, run oppr on them, return result
    def getValue(self) -> int:
        # get values from parents
        parents = super().getParents()
        values = []
        for parent in parents:
            values.append(parent.getValue())
        # must be NOT
        if len(parents) == 1:
            return ~values[0]
        # AND
        elif self.oppr == "AND":
            return values[0] & values[1]
        # LSHIFT
        elif self.oppr == "LSHIFT":
            return values[0] << values[1]
        # RSHIFT
        elif self.oppr == "RSHIFT":
            return values[0] >> values[1]
        # OR
        else:
            return values[0] | values[1]

    # inherited 
    def addParent(self, parent):
        super().addParent(parent)
