import re

with open('day04.txt', 'r') as f:
    input = f.read().split('\n\n')


def parse_passports():
    passports = []
    for line in input:
        passport = {}
        for pair in re.split('[ \n]', line.strip()):
            passport[pair.split(':')[0]] = pair.split(':')[1]
        passports.append(passport)
    return passports


def validate(passport, constraints):
    for field, regex in constraints.items():
        if not re.match(regex, passport.get(field) or ''):
            return False
    return True


print("\n# Part 1")
valid_passports = 0
CONSTRAINTS = {
    'byr': r'.+',
    'iyr': r'.+',
    'eyr': r'.+',
    'hgt': r'.+',
    'hcl': r'.+',
    'ecl': r'.+',
    'pid': r'.+',
}
for passport in parse_passports():
    valid_passports += validate(passport, CONSTRAINTS)
print("Valid passports: {}".format(valid_passports))

print("\n# Part 2")
valid_passports = 0
CONSTRAINTS = {
    'byr': r'^(19[2-8][0-9]|199[0-9]|200[0-2])$',  # four digits; at least 1920 and at most 2002.
    'iyr': r'^(201[0-9]|2020)$',  # (Issue Year) - four digits; at least 2010 and at most 2020.
    'eyr': r'^(202[0-9]|2030)$',  # four digits; at least 2020 and at most 2030.
    'hgt': r'^((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)$',  # a number followed by either cm or in:
    #    If cm, the number must be at least 150 and at most 193.
    #    If in, the number must be at least 59 and at most 76.
    'hcl': r'^#[0-9a-f]{6}$',  # a # followed by exactly six characters 0-9 or a-f.
    'ecl': r'^(amb|blu|brn|gry|grn|hzl|oth)$',  # exactly one of: amb blu brn gry grn hzl oth.
    'pid': r'^\d{9}$',  # a nine-digit number, including leading zeroes.
}
for passport in parse_passports():
    valid_passports += validate(passport, CONSTRAINTS)
print("Valid passports: {}".format(valid_passports))
