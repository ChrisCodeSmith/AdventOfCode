import functools


def part1(_groups):
    _sum = 0
    _groups = [x.replace('\n', '') for x in _groups]
    for group in _groups:
        _sum = _sum + len(set(group))
    print(f"Part 1: {_sum}")


def part2(_groups):
    _sum = 0
    _groups = [group.split('\n') for group in _groups]
    for group in _groups:
        _sum = _sum + len(functools.reduce(lambda x, y: set(x) & set(y), group))
    print(f"sum: {_sum}")


with open(file='05_input.txt', mode='r') as f:
    groups = f.read().split('\n\n')

    # part1(groups)
    part2(groups)
