with open('day09.txt', 'r') as f:
    input = [int(line.strip()) for line in f.readlines()]


def check_previous(numbers, sum):
    for i in range(len(numbers)):
        for k in range(i + 1, len(numbers)):
            if numbers[i] + numbers[k] == sum:
                return True
    return False


def find_window(number):
    for i in range(len(input)):
        window = []
        for k in range(i, len(input)):
            value = input[k]
            window.append(value)
            s = sum(window)
            if s == number:
                return window
            if s > number:
                break


print("\n# Part 1")
PREAMBLE_LENGTH = 25
for i, number in enumerate(input[PREAMBLE_LENGTH:], PREAMBLE_LENGTH):
    if not check_previous(input[i - PREAMBLE_LENGTH:i], number):
        break
print("Invalid number: {}".format(number))

print("\n# Part 2")
window = find_window(number)
print("Result: {}".format(min(window) + max(window)))
