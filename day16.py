class Rule:
    def __init__(self, field: str, ranges: list):
        self.__field = field
        self.__ranges = ranges

    def is_valid(self, value):
        for range in self.__ranges:
            lower = int(range.split('-')[0])
            upper = int(range.split('-')[1])
            if lower <= value <= upper:
                return True
        return False


class Ticket:
    def __init__(self, values: list):
        self.__values = values

    def __matches_rule(value):
        for rule in rules:
            if rule.is_valid(value):
                return True
        return False

    def get_error_rate(self):
        error_rate = 0
        for value in self.__values:
            if not Ticket.__matches_rule(value):
                error_rate += value
        return error_rate


rules = []
my_ticket: Ticket
nearby_tickets = []

with open('day16.txt', 'r') as f:
    sections = f.read().split('\n\n')

    # Parse rules
    for line in sections[0].split('\n'):
        s = line.split(': ')
        ranges = s[1].split(' or ')
        rules.append(Rule(s[0], ranges))

    # Parse my ticket
    my_ticket = Ticket([int(value) for value in sections[1].split('\n')[1].split(',')])

    # Parse nearby tickets
    for line in sections[2].split('\n')[1:-1]:
        nearby_tickets.append(Ticket([int(value) for value in line.split(',')]))

print("\n# Part 1")
error_rate = 0
for ticket in nearby_tickets:
    error_rate += ticket.get_error_rate()
print("Error rate:", error_rate)
