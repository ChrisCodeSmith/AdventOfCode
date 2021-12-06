import re

pat = re.compile('([0-9]*) ([a-z]* [a-z]*) bags?[.,]?')


def read_bag(color: str, _data: list, _processed: list):
    occourences = 0
    if color in _processed:
        return occourences
    _processed.append(color)
    for line in _data:
        if color in line.partition(' bags contain ')[2]:
            occourences += read_bag(line.partition(' bags contain ')[0], _data, _processed)
    return occourences + 1


def part2(color: str, data: list):
    ret = 0
    for line in data:
        if color in line.partition(' bags contain ')[0]:
            matches = pat.findall(line)
            for m in matches:
                if m[1] == 'no other':
                    continue
                ret = ret + int(m[0]) * part2(m[1], data)
    return ret +1


with open('06_input.txt', 'r') as f:
    data = f.read().split('\n')

    # part1:
    #processed = []
    #amount = read_bag('shiny gold', data, processed)
    #print(f"Part1: {amount -1}")

    # part2:
    ret = part2('shiny gold', data)
    print(f"Part2: {ret-1}")


