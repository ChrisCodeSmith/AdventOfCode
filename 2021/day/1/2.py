with open('input.txt', 'r') as f:
    measurements = f.read().splitlines()

    # This is the main thing of part 2:
    #
    # We solve it with a list comprehension: we loop over the origin list and sum the numbers from i to i+3
    # We use the map function inside the sum function to convert the strings to integers.

    triple_mes = [sum(map(int, measurements[i:i+3]))
                  for i in range(0, len(measurements), 1)]

    # we copy the counter from the first part of day 1 - we could write a reusable function, but since we only use it twice and its only for one challenge, we are fine.
    counter = -1
    tmp = 0
    for measurement in triple_mes:
        if int(measurement) > tmp:
            counter += 1
        tmp = int(measurement)

    print(counter)
