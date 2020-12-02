from collections import namedtuple
import re

with open('day2.txt', 'r') as f:
    input = [line.strip().split(" ") for line in f.readlines()]


def parse_policies():
    Policy = namedtuple('Policy', 'char min max password')
    policies = []
    for line in input:
        policies.append(Policy(line[1][:-1], int(line[0].split("-")[0]), int(line[0].split("-")[1]), line[2]))
    return policies


def validate_part_one(policy):
    occurrences = re.sub('[^' + policy.char + ']', '', policy.password)
    return policy.min <= len(occurrences) <= policy.max


def validate_part_two(policy):
    return (policy.password[policy.min - 1] == policy.char) != (policy.password[policy.max - 1] == policy.char)


print("\n# Part 1")
policies = parse_policies()
valid_passwords = 0
for policy in policies:
    if validate_part_one(policy):
        valid_passwords += 1
print("Number of valid passwords: {}".format(valid_passwords))

print("\n# Part 2")
valid_passwords = 0
for policy in policies:
    if validate_part_two(policy):
        valid_passwords += 1
print("Number of valid passwords: {}".format(valid_passwords))
