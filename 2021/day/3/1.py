# helper function to convert a list of binaries to a decimal number.
#
# how it works: e.g. bin is [1,0,1,0], then we start from the end(reversed) 0*2**0, 1*2**1, 0*2**2, 1*2**3 [value*2**position].
# Use the sum function to add each of the values.
def bin_to_dec(bin):
    """ parameters: bin: list -> returns int"""
    return sum(value*2**position for position, value in enumerate(reversed(bin)))


# My algorithm:
#
# Make a list with the size of line length and fill it with 0.
# Iterate over the lines and sum every position of the line to the sums list.
# If the item in the list is greater than the half of all lines, it becomes a 1, else a 0. We get a list with the binary number.
# Use funciont we define above and multipy the decimal numbers to get the solution.
with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    num_of_lines = len(lines)
    n = len(lines[0])
    sums = [0] * n

    # fill sums list.
    for line in lines:
        line = [char for char in line]
        for i in range(0, n):
            sums[i] += int(line[i])

    gamma_rate = [0 if x < num_of_lines/2 else 1 for x in sums]
    epsilon_rate = [1 if x < num_of_lines/2 else 0 for x in sums]

    print(bin_to_dec(gamma_rate)*bin_to_dec(epsilon_rate))
