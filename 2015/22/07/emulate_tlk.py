""" Contains all objects needed to emulate little Bobby Table's wire toy """

""" Describes all nodes in the wire toy """
#Abstract
class InformalNodeInterface:
    """ Every node needs to be made with its label """
    def __init__(self, label):
        self.label = label # Label of the node. int for literals, str for non-literals

    """ Every node needs to return an int value at some point """
    def getValue(self) -> int:
        pass

""" Represents literal value nodes """
#Tangable
class Literal(InformalNodeInterface):
    def __init__(self, value: int):
        super().__init__(value) # for literals: label is just the value

    def getValue(self) -> int:
        return self.label

""" Describes all non-literal nodes """
#Abstract
class InformalNonLiteralInterface(InformalNodeInterface):
    def __init__(self, label: str):
        super().__init__(label) # label must be a string for non-literals
        self.parents = []

    def addParent(self, parent: InformalNodeInterface):
        self.parents.append(parent)

    def getParents(self) -> list[InformalNodeInterface]:
        return self.parents

    #Inherits getValue from abstract node 

""" Represents a wire node. Wires must have a single parent."""
#Tangable
class Wire(InformalNonLiteralInterface):
    #Inherits __init__

    #Inherits getters and setters for parents

    #Wires simply ask their single parent for a value
    def getValue(self) -> int:
        return self.parents[0].getValue()

""" The following five classes are Opperation nodes. They varry only by number of parents (1-2) and getValue logic """

""" bitwise AND opperation node, 2 parents """
class AND(InformalNonLiteralInterface):
    #Inherits __init__

    #Inherits getters and setters for parents

    """ Gets value with bitwise AND of parents' values """
    def getValue(self) -> int:
        return self.parents[0].getValue() & self.parents[1].getValue()

""" bitwise NOT opperation node, 1 parent """
class NOT(InformalNonLiteralInterface):
    #Inherits __init__

    #Inherits getters and setters for parents

    """ Gets value with bitwise NOT of parent's value """
    def getValue(self) -> int:
        return (1 << 16) - 1 - self.parents[0].getValue()

""" bitwise LSHIFT opperation node, 2 parents """
class LSHIFT(InformalNonLiteralInterface):
    #Inherits __init__

    #Inherits getters and setters for parents

    """ Gets value with bitwise leftshift of parents' values """
    def getValue(self) -> int:
        return self.parents[0].getValue() << self.parents[1].getValue()

""" bitwise RSHIFT opperation node, 2 parents """
class RSHIFT(InformalNonLiteralInterface):
    #Inherits __init__

    #Inherits getters and setters for parents

    """ Gets value with bitwise rightshift of parents' values """
    def getValue(self) -> int:
        return self.parents[0].getValue() >> self.parents[1].getValue()

""" bitwise OR opperation node, 2 parents """
class OR(InformalNonLiteralInterface):
    #Inherits __init__

    #Inherits getters and setters for parents

    """ Gets value with bitwise or of parents' values """
    def getValue(self) -> int:
        return self.parents[0].getValue() | self.parents[1].getValue()
