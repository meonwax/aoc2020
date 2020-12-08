with open('day08.txt', 'r') as f:
    input = [line.strip() for line in f.readlines()]


def run():
    processed_line_numbers = set()
    a = 0
    pc = 0
    while pc < len(input):
        if pc in processed_line_numbers:
            return a, True
        processed_line_numbers.add(pc)
        op, arg = input[pc].split(' ')
        if op == 'acc':
            a += int(arg)
        elif op == 'jmp':
            pc += int(arg)
            continue
        pc += 1
    return a, False


def flip_operation(line_number):
    if input[line_number].startswith('jmp'):
        input[line_number] = input[line_number].replace('jmp', 'nop')
    elif input[line_number].startswith('nop'):
        input[line_number] = input[line_number].replace('nop', 'jmp')


print("\n# Part 1")
a = run()[0]
print("Accumulator value: {}".format(a))

print("\n# Part 2")
for line_number in range(0, len(input)):
    a, infinite_loop = run()
    if infinite_loop:
        flip_operation(line_number - 1)  # Unflip last operation
        flip_operation(line_number)  # Flip current operation
print("Accumulator value: {}".format(a))
