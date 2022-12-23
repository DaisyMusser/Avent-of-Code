
import sys

data = open("input.txt").read()
data = data.split("\n")

nice_count = 0

for line in data:
    # nice strings needs both (1) and (2) to be true
    # (1) contains a pair of any two letters that appear more than once in the string, eg: sy, sy
    passed_1 = False
    # for every two letter group in string...
    for i in range(len(line) - 1):
        # end this check if already passed
        if passed_1:
            break
        pair = line[i] + line[i + 1]
        # remove that group, split string into two substring (one or more might be empty)
        subStrings = []
        if (i > 1):
            # need a starting substring
            subStrings.append(line[:i])
        if (i < len(line) - 3):
            # need an ending substring
            subStrings.append(line[i + 2:])
        # check if the two letter group is found in some substring
        for sub in subStrings:
            if passed_1:
                break
            for ii in range(len(sub) - 1):
                # if found, set passed_1 to true, break out of (1) for loop 
                checkPair = sub[ii] + sub[ii + 1]
                if (checkPair == pair):
                    passed_1 = True
                    break
    if not passed_1:
        # naughty
        continue

    # (2) contains one letter which repeats with any other letter between, eg: aya, xxx
    passed_2 = False
    # for every letter
    for i in range(len(line) - 2):
        # check if letter two after matches
        if line[i] == line[i + 2]:
            # if yes, passed (2)
            passed_2 = True
            break

    if not passed_2:
        continue

    nice_count += 1

print(nice_count)

