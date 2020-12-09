def slope(d_x, d_y):
    y = 0
    line_length = len(lines[0])
    tree_count = 0
    for x in range(0, len(lines), d_x):
        if lines[x][y] == '#':
            tree_count += 1
        y = (y + d_y) % line_length
    return tree_count


with open('02_input.txt', 'r') as f:
    lines = f.readlines()
    lines = list(map(lambda a: a.strip(), lines))
    print(f"Tree count: {slope(1,3)}")
    slope1 = slope(1, 1)
    slope2 = slope(1, 3)
    slope3 = slope(1, 5)
    slope4 = slope(1, 7)
    slope5 = slope(2, 1)
    print(f"DAFUQ: {slope1*slope2*slope3*slope4*slope5}")