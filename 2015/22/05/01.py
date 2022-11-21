
data = open("input.txt").read()
data = data.split("\n")
for line in data:
	passed_one = False
	# unless...
	# rule 1: must be xxybkxx or xxxx not xxx for some x
    # get all unique letters
    line_list = [*line]
    char_set = set(line_list)
    for letter in char_set:
        # only check next letter if we havn't passed rule one yet
        if not passed_one:
            all_runs = {}
            current_run = 1
            # don't consider the last char in line
            for i, other_letter in enumerate(line_list[:-1]):
                if other_letter == letter:
                    if other_letter == char_set[i + 1]:
                        # next matches
                        current_run += 1
                    else:
                        # next doesn't match
                        if current_run > 1:
                            # we have some run
                            tag = str(current_run)
                            current_run = 1
                            if tag in all_runs.keys():
                                all_runs[tag] += 1
                            else:
                                all_runs[tag] = 1

