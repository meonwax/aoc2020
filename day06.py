with open('day06.txt', 'r') as f:
    input = f.read().strip().split('\n\n')

print("\n# Part 1")
sum = 0
for group in input:
    answers = set()
    for person in group.split('\n'):
        for answer in person:
            answers.add(answer)
    sum += len(answers)
print("Sum: {}".format(sum))

print("\n# Part 2")
sum = 0
for group in input:
    answers = {}
    persons = group.split('\n')
    for person in persons:
        for answer in person:
            if answer in answers:
                answers[answer] += 1
            else:
                answers[answer] = 1
    for count in answers.values():
        sum += count == len(persons)
print("Sum: {}".format(sum))
