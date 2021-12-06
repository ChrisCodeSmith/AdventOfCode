
with open('00_input.txt', 'r') as f:
    lines = f.readlines()
    lines = set(map(lambda x: int(x.strip()), lines))
    first = -1
    second = -1
    for line in lines:
        if 2020-int(line) in lines:
            first = line
            break
    for line in lines:
        if first+line == 2020:
            second = line
            break
    print(f"{first} + {second} = {first+second} || mul: {first*second}")