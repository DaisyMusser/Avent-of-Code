""" Contains all objects needed to emulate little Bobby Table's wire toy """


""" Describes all nodes in the wire toy """
#Abstract
class InformalNodeInterface:
    """ Every node needs to return an int value at some point """
    def getValue(self) -> int:
        pass


""" Represents literal value nodes """
#Tangable
class Literal(InformalNodeInterface):
    def __init__(self, value: int):
        self.value = value

    def getValue(self) -> int:
        return self.value


""" Describes all non-literal nodes """
#Abstract
class InformalNonLiteralInterface(InformalNodeInterface):
    def __init__(self):
        self.parents = []
        self.value = None

    def addParent(self, parent: InformalNodeInterface):
        self.parents.append(parent)

    def getParents(self) -> list[InformalNodeInterface]:
        return self.parents

    #Inherits getValue from abstract node 


""" Represents a wire node. Wires must have a single parent."""
#Tangable
class Wire(InformalNonLiteralInterface):
    def __init__(self, label: str):
        super().__init__()
        self.label = label

    #Inherits getters and setters for parents

    #Wires simply ask their single parent for a value
    def getValue(self) -> int:
        if self.value == None:
            self.value = self.parents[0].getValue()
        return self.value


""" The following five classes are Opperation nodes. They varry only by number of parents (1-2) and getValue logic """

""" bitwise AND opperation node, 2 parents """
#Tangable
class AND(InformalNonLiteralInterface):
    def __init__(self, a: InformalNodeInterface, b: InformalNodeInterface):
        super().__init__()
        self.parents = [a, b]

    #Inherits getters and setters for parents

    """ Gets value with bitwise AND of parents' values """
    def getValue(self) -> int:
        if self.value == None:
            self.value = self.parents[0].getValue() & self.parents[1].getValue()
        return self.value


""" bitwise NOT opperation node, 1 parent """
#Tangable
class NOT(InformalNonLiteralInterface):
    def __init__(self, a: InformalNodeInterface):
        super().__init__()
        self.parents = [a]

    #Inherits getters and setters for parents

    """ Gets value with bitwise NOT of parent's value """
    def getValue(self) -> int:
        if self.value == None:
            self.value = (1 << 16) - 1 - self.parents[0].getValue()
        return self.value


""" bitwise LSHIFT opperation node, 2 parents """
#Tangable
class LSHIFT(InformalNonLiteralInterface):
    def __init__(self, a: InformalNodeInterface, b: InformalNodeInterface):
        super().__init__()
        self.parents = [a, b]

    #Inherits getters and setters for parents

    """ Gets value with bitwise leftshift of parents' values """
    def getValue(self) -> int:
        if self.value == None:
            self.value = self.parents[0].getValue() << self.parents[1].getValue()
        return self.value


""" bitwise RSHIFT opperation node, 2 parents """
#Tangable
class RSHIFT(InformalNonLiteralInterface):
    def __init__(self, a: InformalNodeInterface, b: InformalNodeInterface):
        super().__init__()
        self.parents = [a, b]

    #Inherits getters and setters for parents

    """ Gets value with bitwise rightshift of parents' values """
    def getValue(self) -> int:
        if self.value == None:
            self.value = self.parents[0].getValue() >> self.parents[1].getValue()
        return self.value


""" bitwise OR opperation node, 2 parents """
#Tangable
class OR(InformalNonLiteralInterface):
    def __init__(self, a: InformalNodeInterface, b: InformalNodeInterface):
        super().__init__()
        self.parents = [a, b]

    #Inherits getters and setters for parents

    """ Gets value with bitwise or of parents' values """
    def getValue(self) -> int:
        if self.value == None:
            self.value = self.parents[0].getValue() | self.parents[1].getValue()
        return self.value


