import functools
import collections
import re

pat = re.compile('([0-9]*) ([a-z]* [a-z]*) bags?[.,]?')

Bag = collections.namedtuple('Bag', ['name', 'contains'])

contains_golden = []
bags = []

def alter_search(color: str, data):
    for line in data:
        print(line) if color in line.partition(' bags contain ')[2] else None


def search_for(color: str, data):
    dime = []
    for line in data:
        matches = pat.findall(line)
        if len(matches) > 0:
            for match in matches:
                if match:
                    #print(match)
                    if color in match[1]:
                        #print(f"{line.partition(' bags contain ')[0]} : {match[0]}: {match[1]}")
                        dime.append((line.partition(' bags contain ')[0], match[0]))

    if len(dime) == 0:
        return 1
    print(f"{color}: {dime}")
    #ret_val = [search_for(x[0], data) for x in dime]

    #print(f"RETVAL{ret_val}")
    retval = 0
    for x in dime:
        retval = retval + search_for(x[0], data) * int(x[1])
    print(f"RET: {retval}")
    return retval



with open('06_input.txt', 'r') as f:
    lines = f.read().strip('.').split('.\n')
    search_for('shiny gold', lines)
    # alter_search('shiny gold', lines)
    # print('------------------------')
    # alter_search('vibrant green', lines)
    # print('------------------------')
    # alter_search('plaid teal', lines)
    # print('------------------------')
    # alter_search('posh aqua', lines)

    # #print(lines)
    # for line in lines:
    #     #print(line if 'shiny gold' in line else None)
    #     #print(line)
    #     bag_color = line.partition(' bags contain ')[0]
    #     contains = line.partition(' bags contain')[2].split(', ')
    #     contains = [tuple(x.strip().split(' ', 1)) for x in contains]
    #     #print(bag_color + " " + str(contains))
    #     bags.append((bag_color, contains))
    # print(bags)
    # #for bag in bags:
    # #    print(bag if 'shiny gold' in bag)