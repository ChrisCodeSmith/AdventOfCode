
with open('00_input.txt', 'r') as f:
    lines = f.readlines()
    lines = list(map(lambda a: int(a.strip()), lines))

    for x in range(0, len(lines)):
        for y in range(x, len(lines)):
            for z in range(y, len(lines)):
                #print(f"({x},{y},{z})")
                if lines[x]+lines[y]+lines[z] == 2020:
                    print(f"{lines[x]}+{lines[y]}+{lines[z]}=2020 || mul: {lines[x]*lines[y]*lines[z]}")
                    break
