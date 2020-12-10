
def is_sum(_preamble, _num):
    for j in range(0, len(_preamble)):
        for k in range(j + 1, len(_preamble)):
            if preamble[j] + preamble[k] == _num:
                return True
    return False


def get_contiguous(_lines, _num):
    for j in range(0, len(_lines)):
        _sum = _lines[j]
        for k in range(j+1, len(_lines)):
            _sum += _lines[k]
            if _sum > _num:
                break
            if _sum == _num:
                subset = _lines[j:k+1]
                return min(subset) + max(subset)
    return None

LEN_PREAMBLE = 25

with open('08_input.txt', 'r') as f:
    lines = f.read().split('\n')
    lines = list(map(lambda x: int(x), lines))
    org_lines = lines.copy()

    preamble = lines[:LEN_PREAMBLE]
    del lines[:LEN_PREAMBLE]

    sol = 0
    for i in range(0, len(lines)):
        #print(f"Preamble: {preamble}, list: {lines}")
        num = lines[0]
        if not is_sum(preamble, num):
            print(f"Part1: This is no sum: {num}")
            sol = num
            break
        preamble = preamble[1:]
        preamble.append(lines[0])
        lines = lines[1:]

    p2 = get_contiguous(org_lines, sol)
    print(f"Part2: The (smallest + largest) number of contiguous set that form the sum of Part1: {p2}")
