

with open('09_test_input_2.txt', 'r') as f:
    lines = f.read().split('\n')
    lines = list(map(lambda x: int(x), lines))
    lines.sort()
    # append the built-int joltage adapter to the list
    lines.append(max(lines) + 3)
    ones = 0
    twos = 0
    threes = 0
    last = 0
    print(lines)
    for line in lines:
        if line - last == 1:
            ones += 1
        elif line - last == 2:
            twos += 1
        elif line - last == 3:
            threes += 1
        last = line
    print(f"1 Jolt diff: {ones}")
    #print(f"2 Jolt diffs: {twos}")
    print(f"3 Jolt diffs: {threes}")
    print(f"mul: {ones*threes}")
