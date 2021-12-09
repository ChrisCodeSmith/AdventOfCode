# pretty the same as in task 1, just add athe aim var and adjust the conditions.

with open('input.txt', 'r') as f:
    instructions = f.read().splitlines()
    depth = 0
    h_pos = 0
    aim = 0

    for instr in instructions:
        cmd = instr.split(' ')
        if cmd[0] == 'forward':
            h_pos += int(cmd[1])
            depth += aim * int(cmd[1])
        elif cmd[0] == 'up':
            aim -= int(cmd[1])
        elif cmd[0] == 'down':
            aim += int(cmd[1])

    print(f"depth: {depth}, horizontal position: {h_pos}")
    print(f"Mul: {depth*h_pos}")
