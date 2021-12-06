def swap_op(ip, data):
    inst = data[ip].split(' ')
    if inst[0] == 'nop':
        data[ip] = f"jmp {inst[1]}"
    elif inst[0] == 'jmp':
        data[ip] = f"nop {inst[1]}"


def eva(data: list, ip: int, acc: int, visited: list, instance: int):
    if instance >1:
        return 'inst', acc
    while True:
        if str(ip) in visited:
            return 'inf', acc
        else:
            visited.append(str(ip))
        if ip > len(data) -1:
            return 'term', acc
        op, arg = data[ip].split(' ')
        if op == 'acc':
            acc += int(arg)
            ip += 1
        elif op == 'nop':
            tmp_lst = data.copy()
            tmp_visited = visited.copy()
            swap_op(ip, tmp_lst)
            ret = eva(tmp_lst, ip+int(arg), acc, tmp_visited, instance+1)
            if ret[0] == 'term':
                return ret
            ip += 1
            continue
        elif op == 'jmp':
            tmp_lst = data.copy()
            tmp_visited = visited.copy()
            swap_op(ip, tmp_lst)
            ret = eva(tmp_lst, ip+1, acc, tmp_visited, instance+1)
            if ret[0] == 'term':
                return ret
            ip = ip + int(arg)
        else:
            break
    #print(acc)

with open('07_input.txt', 'r') as f:
    lines = f.read().split('\n')

    ret = eva(lines, 0, 0, [], 0)
    print(ret)

