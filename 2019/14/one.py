# day 14: how much ore is needed for fuel?

# file io
def grab_input(file_name):
    reactions = []
    with open(file_name) as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            reactions.append(line)
    return reactions


# main program
raw = grab_input('input.txt')      # change file_name here 
print(raw)           
            
