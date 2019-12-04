# gets input
def file_reader(file_name):
    with open(file_name) as fp:
        while True:
            line = fp.read()
            if not line:
                break
            input = line
            hyphen = input.find('-')
            input.replace(input[hyphen], '')  # code from: https://www.journaldev.com/23674/python-remove-character-from-string#python-remove-character-from-string

    return input



# main program
range = file_reader('input.txt')
print(range)
