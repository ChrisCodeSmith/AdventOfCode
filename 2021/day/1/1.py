# We read the lines from input.txt and iterate over every line and compare it to a tmp var, which is initially 0,
# but gets updated at the end of every iteration with its measurement.
# So after the first iteration it always contains the measurement of the previous iteration.
#
# We count each time the actual measurement is greater than the one before.


with open('input.txt', 'r') as f:
    measurements = f.read().splitlines()

    counter = -1  # -1 becuz the first element is smaller than 0 and we count it even thou we shouldn't
    tmp = 0
    for measurement in measurements:
        if int(measurement) > tmp:
            counter += 1
        tmp = int(measurement)

    print(counter)
