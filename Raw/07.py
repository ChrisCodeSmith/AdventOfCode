
def part1():
    with open('07_input.txt', 'r') as f:
        lines = f.read().split('\n')
        visited = []
        acc = 0
        ip = 0
        while True:
            if str(ip) in visited:
                break
            else:
                visited.append(str(ip))
            op, arg = lines[ip].split(' ')
            if op == 'acc':
                acc += int(arg)
                ip += 1
            elif op == 'nop':
                ip += 1
                continue
            elif op == 'jmp':
                ip = ip + int(arg)
            else:
                break
        print(acc)



part1()
