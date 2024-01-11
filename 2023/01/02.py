# checks if number is written out in line. If true returns number as int and start index of line
def isStrNumber(line: str):
    numbers = {
            "one"   : "1",
            "two"   : "2", 
            "three" : "3", 
            "four"  : "4", 
            "five"  : "5",
            "six"   : "6", 
            "seven" : "7", 
            "eight" : "8", 
            "nine"  : "9"} 
    found_numbers = {}
    for number in numbers:
        if number in line:
            found_numbers[line.find(number)] = numbers[number]
    if found_numbers:
        i = sorted(found_numbers.keys())[0]
        return found_numbers[i], i
    return False

# same as above but starts reading the end of line. Returns ending index of the number that is written out.
def isStrNumberRev(line: str):
    numbers = {
            "one"   : "1",
            "two"   : "2", 
            "three" : "3", 
            "four"  : "4", 
            "five"  : "5",
            "six"   : "6", 
            "seven" : "7", 
            "eight" : "8", 
            "nine"  : "9"} 
    found_numbers = {}
    for number in numbers:
        if number in line:
            starti = line.rfind(number)
            endi = starti + len(number)
            found_numbers[endi] = numbers[number]
    if found_numbers: # empty dictionaries are False, I love python
        i = sorted(found_numbers.keys()).pop()
        # return number and last index
        return found_numbers[i], i
    return False

def isIntNumber(line: str):
    # or return number(str) and index
    for i, char in enumerate(line):
        if char in "0123456789":
            return char, i
    return False

def isIntNumberRev(line: str):
    # or return number(str) and index
    i = len(line) - 1
    while i > -1:
        if line[i] in "0123456789":
            return line[i], i
        i -= 1
    return False


if __name__ == "__main__":
    lines = open("input.txt").read().split("\n")
    lines.remove("") # remove empty string that at the end of input
    total = 0

    # TODO
#    lines = ["eightwothree"]

    for line in lines:

        # find tensDigit
        if isStrNumber(line):
            if isIntNumber(line):
                strNumber, str_i = isStrNumber(line)
                intNumber, int_i = isIntNumber(line)
                if str_i < int_i:
                    tensDigit = strNumber
                else:
                    tensDigit = intNumber
            else:
                tensDigit, i = isStrNumber(line)
        else:
            tensDigit, i = isIntNumber(line)


        # find onesDigit
        if isStrNumberRev(line):
            if isIntNumberRev(line):
                strNumber, str_i = isStrNumberRev(line)
                intNumber, int_i = isIntNumberRev(line)
                if str_i > int_i:
                    onesDigit = strNumber
                else:
                    onesDigit = intNumber
            else:
                onesDigit, i = isStrNumberRev(line)
        else:
            onesDigit, i = isIntNumberRev(line)

        # combine digits into two digit number, add to sum total
        calibraton_val = int(tensDigit + onesDigit)
        total += calibraton_val

        # TODO
        print(str(calibraton_val))

    print("Total: " + str(total))

# I know the answer is between 46195 and 56108
# 200 is too low, as you would expect. Made some mistake here...
