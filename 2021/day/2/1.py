# split every line into command and parameter: decide what to do based on instruction and calculate the depth and horizontal position.

with open('input.txt', 'r') as f:
    instructions = f.read().splitlines()
    depth = 0
    h_pos = 0

    for instr in instructions:
        cmd = instr.split(' ')
        if cmd[0] == 'forward':
            h_pos += int(cmd[1])
        elif cmd[0] == 'up':
            depth -= int(cmd[1])
        elif cmd[0] == 'down':
            depth += int(cmd[1])

    print(f"depth: {depth}, horizontal position: {h_pos}")
    print(f"Mul: {depth*h_pos}")
