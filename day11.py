with open('day11.txt', 'r') as f:
    input = [line.strip() for line in f.readlines()]


def deep_copy(list):
    copy = []
    for r in list:
        row = []
        for s in r:
            row.append(s)
        copy.append(row)
    return copy


DIRECTIONS = [
    (-1, -1),  # North-West
    (-1, 0),  # North
    (-1, 1),  # North-East
    (0, -1),  # West
    (0, 1),  # East
    (1, -1),  # South-West
    (1, 0),  # South
    (1, 1),  # Sout-East
]


def find_occupied_neighbours(layout, direction, r, s, unlimited):
    while True:
        r = r + direction[0]
        s = s + direction[1]
        if r < 0 or s < 0 or r >= len(layout) or s >= len(layout[r]):
            return 0
        seat = layout[r][s]
        if seat == '.':
            if unlimited:
                continue
            return 0
        if seat == 'L':
            return 0
        if seat == '#':
            return 1


def count_occupied_neighbours(layout, r, s, unlimited):
    seat = layout[r][s]
    count = 0
    if seat != '.':
        for direction in DIRECTIONS:
            count += find_occupied_neighbours(layout, direction, r, s, unlimited)
    return count


def next_round(last_layout, max_neighbours, unlimited):
    new_layout = deep_copy(last_layout)
    for r in range(len(new_layout)):
        row = new_layout[r]
        for s in range(len(row)):
            seat = row[s]
            if seat == '.':
                continue
            occupied_neighbours = count_occupied_neighbours(last_layout, r, s, unlimited)
            if seat == 'L' and occupied_neighbours == 0:
                new_layout[r][s] = '#'
            elif seat == '#' and occupied_neighbours > max_neighbours:
                new_layout[r][s] = 'L'
    return new_layout


def count_occupied_seats(layout):
    occupied_count = 0
    for row in layout:
        for seat in row:
            occupied_count += seat == '#'
    return occupied_count


print("\n# Part 1")
last_layout = deep_copy(input)
while True:
    new_layout = next_round(last_layout, 3, False)
    if new_layout == last_layout:
        break
    last_layout = new_layout
print("Number of seats occupied: {}".format(count_occupied_seats(last_layout)))

print("\n# Part 2")
last_layout = deep_copy(input)
while True:
    new_layout = next_round(last_layout, 4, True)
    if new_layout == last_layout:
        break
    last_layout = new_layout
print("Number of seats occupied: {}".format(count_occupied_seats(last_layout)))
