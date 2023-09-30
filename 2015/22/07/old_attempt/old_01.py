
from tqdm import tqdm

# poor form? idk...
# mem maps terms (strings) to values (ints)
mem = {}

# takes a term and returns its value
def simpTerm(term):
    if isinstance(term, int):
        return term
    else:
        # is int
        if not term in mem.keys():
            mem[term] = 0
        return mem[term] 

def rSimplify(terms):
    if terms == [""]:
        return 0 
    addr = terms[len(terms) - 1]
    # terms looks like ["123", "AND", "y", "->", "e"]
    # turn all strings to ints where needed
    for i, term in enumerate(terms):
        if not isinstance(term, int):
            if term in "0123456789":
                terms[i] = int(term)
    # base case:
    if len(terms) == 3:
        if not isinstance(terms[0], int):
            terms[0] = simpTerm(terms[0])
        mem[addr] = terms[0]
    # recusive case:
    else:
        # possible opperations:

        # AND    - bitwise and
        # LSHIFT - left-shift
        # RSHIFT - right-shift
        # NOT    - bitwise complement
        # OR     - bitwise or

        # special case for NOT
        if terms[0] == "NOT":
            val = ~simpTerm(terms[1])
            reduced_terms = [val, "->", addr]
            return rSimplify(reduced_terms)
        # all other oppr 
        else:
            oppr = terms[1]
            val1 = int(simpTerm(terms[0]))
            val2 = int(simpTerm(terms[2]))
            if oppr == "AND":
                val = val1 & val2
            elif oppr == "LSHIFT":
                val = val1 << val2
            elif oppr == "RSHIFT":
                val = val1 >> val2
            else: # OR
                val = val1 | val2
            reduced_terms = [val, "->", addr]
            return rSimplify(reduced_terms)


data = open("example.txt").read()
data = data.split("\n")
for line in tqdm(data):
    terms = line.split(" ")
    rSimplify(terms)
print(mem["a"])

