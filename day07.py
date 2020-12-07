import re

with open('day07.txt', 'r') as f:
    input = [line.strip() for line in f.readlines()]


def parse_rules(input):
    rules = {}
    for rule in input:
        matches = re.search(r'(.+) bags contain (.+)\.', rule)
        bag = matches.group(1)
        children = {}
        if matches.group(2) != 'no other bags':
            for child in matches.group(2).split(', '):
                matches = re.search(r'(\d+) (.+) ', child)
                children[matches.group(2)] = int(matches.group(1))
        rules[bag] = children
    return rules


def calculate_bag(bag):
    bags = set()
    for key, value in rules.items():
        if bag in value.keys():
            bags.add(key)
            bags.update(calculate_bag(key))
    return bags


def calculate_containing_bags(bag):
    count = 0
    for child, amount in rules.get(bag).items():
        count += amount
        count += amount * calculate_containing_bags(child)
    return count


rules = parse_rules(input)

print("\n# Part 1")
print("Number of bag colors: {}".format(len(calculate_bag('shiny gold'))))

print("\n# Part 2")
print("Number of containing bags: {}".format(calculate_containing_bags('shiny gold')))
