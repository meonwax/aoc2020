with open('day10.txt', 'r') as f:
    input = [int(line) for line in f.readlines()]

# input = [int(i) for i in """16
# 10
# 15
# 5
# 1
# 11
# 7
# 19
# 6
# 12
# 4""".split()]

joltage_diff_count = {
    1: 0,
    3: 0,
}

print("\n# Part 1")
input.sort()
joltage = 0
for adapter in input:
    diff = adapter - joltage
    joltage_diff_count[diff] += 1
    joltage += diff
joltage_diff_count[3] += 1

print("Result: {}".format(joltage_diff_count[1] * joltage_diff_count[3]))
