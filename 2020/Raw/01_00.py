with open('01_input.txt', 'r') as f:
    lines = f.readlines()
    #print(lines)
    #print(len(lines))
    valid_count = 0
    for line in lines:
        line = line.split(' ')
        letter_occurrence = line[2].count(line[1].rstrip(':'))
        min = line[0].split('-')[0]
        max = line[0].split('-')[1]
        #print(f"{line} || {letter_occurrence}, min: {min}, max: {max}")
        if letter_occurrence >= int(min) and letter_occurrence <= int(max):
            valid_count += 1
    print(f"valid pws: {valid_count}")