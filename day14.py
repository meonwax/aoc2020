import re

with open('day14.txt', 'r') as f:
    input = [line.strip() for line in f.readlines()]


def apply_bit(value: int, index: int, bit: str):
    binary_string = '{0:036b}'.format(value)
    binary_string = binary_string[:index] + bit + binary_string[index + 1:]
    return int(binary_string, 2)


def generate_variation(address: int, floating_bits: list, index: int, value: int):
    if index < len(floating_bits):
        bit_position = floating_bits[index]

        variation_address = apply_bit(address, bit_position, '0')
        generate_variation(variation_address, floating_bits, index + 1, value)

        variation_address = apply_bit(address, bit_position, '1')
        generate_variation(variation_address, floating_bits, index + 1, value)
    else:
        mem[address] = value


print("\n# Part 1")
mask: str
mem = {}
for line in input:
    if line.startswith('mask'):
        mask = re.search(r'^mask = ([X\d]+)$', line).group(1)
    else:
        matches = re.search(r'^mem\[(\d+)\] = (\d+)$', line)
        value = int(matches.group(2))
        for i, char in enumerate(mask):
            if char != 'X':
                value = apply_bit(value, i, char)
        address = int(matches.group(1))
        mem[address] = value
print("Sum:", sum(mem.values()))

print("\n# Part 2")
mem = {}
for line in input:
    if line.startswith('mask'):
        mask = re.search(r'^mask = ([X\d]+)$', line).group(1)
    else:
        matches = re.search(r'^mem\[(\d+)\] = (\d+)$', line)
        address = int(matches.group(1))
        value = int(matches.group(2))
        floating_bits = []
        for i, char in enumerate(mask):
            if char == '1':
                address = apply_bit(address, i, '1')
            if char == 'X':
                floating_bits.append(i)
        generate_variation(address, floating_bits, 0, value)
print("Sum:", sum(mem.values()))
