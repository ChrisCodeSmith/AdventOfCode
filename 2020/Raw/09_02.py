with open('09_test_input_2.txt', 'r') as f:
    lines = f.read().split('\n')
    lines = list(map(lambda x: int(x), lines))
    lines.sort()
    # append the built-int joltage adapter to the list
    lines.append(max(lines) + 3)
    print(lines)

    result = 1
    i = 0
    while i < len(lines)-3:
        print(i)
        coherent = 0
        diff = lines[i+1] - lines[i]
        if diff <= 3:
            if lines[i+2] - lines[i] <= 2:
                if lines[i+3] - lines[i] <= 3:
                    print("3")
                    result += 3
                    i += 1
                    continue
                print("2")
                result += 2
        i += 1
        #print(diff)
    print(result)
