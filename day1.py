with open('day1.txt', 'r') as f:
    input = [int(line) for line in f.readlines()]

print("\n# Part 1")
for i, v1 in enumerate(input):
    for v2 in input[i + 1:]:
        if v1 + v2 == 2020:
            print("{} + {} = {}".format(v1, v2, v1 + v2))
            print("{} * {} = {}".format(v1, v2, v1 * v2))

print("\n# Part 2")
for i, v1 in enumerate(input):
    for k, v2 in enumerate(input[i + 1:]):
        if v1 + v2 >= 2020:
            continue
        for v3 in input[k + 1:]:
            if v1 + v2 + v3 == 2020:
                print("{} + {} + {} = {}".format(v1, v2, v3, v1 + v2 + v3))
                print("{} * {} * {} = {}".format(v1, v2, v3, v1 * v2 * v3))
