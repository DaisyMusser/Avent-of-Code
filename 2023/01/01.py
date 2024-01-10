
if __name__ == "__main__":
    lines = open("input.txt").read().split("\n")
    lines.remove("") # remove empty string that at the end of input

    total = 0

    for line in lines:
        # walk through line forwards taking first digit
        i = 0
        char = line[i]
        while not char in "0123456789":
            i += 1
            char = line[i]
        tensDigit = char
        # walk through line backwards taking first digit
        i = -1
        char = line[i]
        while not char in "0123456789":
            i -= 1
            char = line[i]
        onesDigit = char
        # combine digits into two digit number, add to sum total
        total += int(tensDigit + onesDigit)

    print("Total: " + str(total))

