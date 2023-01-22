
# emulates little Bobby table's circut toy



# generic nodes need to know their parents
class node(object):
    def __init__(self):
        self.parents = []

    def addParent(self, parent):
        self.parents.append(parent)

# specific node type: address
# has a value and a name
# one parent
class address(node):
    def __init__(self, name):
        super().__init__()
        # specific stuff
        self.name  = name
        self.value = None

    # set addr to some value
    def set(self, val):
        self.value = val

    # read value stored at this addr
    def read(self):
        return self.value
    
    # inherited 
    def addParent(self, parent):
        super().__init__(parent)

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
    def run(self):
        parents = super().parents
        # must be NOT
        if len(parents) == 1:
            return ~parents[0]
        # AND
        elif self.oppr == "AND":
            return parents[0] & parents[1]
        # LSHIFT
        elif self.oppr == "LSHFIT":
            return parents[0] << parents[1]
        # RSHIFT
        elif self.oppr == "RSHFIT":
            return parents[0] >> parents[1]
        # OR
        else:
            return parents[0] | parents[1]

    # inherited 
    def addParent(self, parent):
        super().__init__(parent)
