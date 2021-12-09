# We read the lines from input.txt and iterate over every line and compare it to a tmp var, which is initially maxint.
# This tmp var gets updated to the actual measurement at the end of each iteration,
# so it has the value of the previous iteration for all calcualtions in the next iteration.
#
# The counter increases everytime the actual measurement is greater than the one before: measurement > tmp

import sys
with open('input.txt', 'r') as f:
    measurements = f.read().splitlines()

    counter = 0
    tmp = sys.maxsize
    for measurement in measurements:
        if int(measurement) > tmp:
            counter += 1
        tmp = int(measurement)

    print(counter)
