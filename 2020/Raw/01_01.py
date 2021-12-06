with open('01_input.txt', 'r') as f:
    lines = f.readlines()
    print(lines)
    valid_count = 0
    valid_pos1 = 0
    valid_pos2 = 0
    for line in lines:
        line = line.split(' ')
        pos1 = int(line[0].split('-')[0])
        pos2 = int(line[0].split('-')[1])
        letter = line[1].strip(':')
        #print(f"pos1:{pos1}, pos2:{pos2}, letter:{letter}, line[pos1]: {line[2][pos1-1]}")
        print(f"{line[2]}: 1st: {pos1}, 2nd: {pos2}")
        #if line[2][pos1-1] == letter or line[2][pos2-1] == letter:
        #    valid_count += 1
        if line[2][pos1-1] == letter:
            valid_pos1 += 1
            if line[2][pos2-1] != letter:
                valid_count += 1
        if line[2][pos2-1] == letter:
            valid_pos2 += 1
            if line[2][pos1-1] != letter:
                valid_count += 1
    print(f"Valid pws: {valid_count}: {valid_pos1}: {valid_pos2}")
