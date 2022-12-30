
from tqdm import tqdm

data = open("input.txt").read()
data = data.split("\n")

char_cnt = 0

for line in tqdm(data):
    # lose start and end quotes
    line = line[1:len(line) - 1]
    # \\   --> \
    # I think i get to skip this one?? seems like python will handle it for me
    # \"   --> '
    # this too?
    # \xAB --> where AB are ascii for one char 
    # this too??
    for char in line:
        char_cnt += 1

print(char_cnt)


