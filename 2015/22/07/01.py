
from tqdm import tqdm

data = open("input.txt").read()
data = data.split("\n")
memory = {}
for line in tqdm(data):
    terms = line.split(" ")
    # {reduces to some value} -> addr to store that value
    # best case: explicit value
    #TODO this might be hex?? include abc.. etc?
    if terms[0][0] in "0123456789" and terms[1] == "->":
        memory[terms[3]] = int(terms[0])
        continue
    # replace addr with value


