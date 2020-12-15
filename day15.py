input = [2, 15, 0, 9, 1, 20]


def play(rounds: int) -> int:
    numbers = {}
    last_number: int
    for turn, number in enumerate(input):
        numbers[number] = [turn]
        last_number = number
    for turn in range(len(input), rounds):
        if last_number not in numbers:
            numbers[last_number] = [turn - 1]
            last_number = 0
        else:
            numbers[last_number].append(turn - 1)
            last_number = numbers[last_number][-1] - numbers[last_number][-2]
    return last_number


print("\n# Part 1")
print("Last number spoken:", play(2020))

print("\n# Part 2")
print("Last number spoken:", play(30000000))
