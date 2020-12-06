with open('day05.txt', 'r') as f:
    input = [line.strip() for line in f.readlines()]


def get_row(boarding_pass):
    lower = 0
    upper = 128
    for i in range(7):
        diff = int((upper - lower) / 2)
        if boarding_pass[i] == 'F':
            upper -= diff
        else:
            lower += diff
    return lower


def get_column(boarding_pass):
    lower = 0
    upper = 8
    for i in range(7, 10):
        diff = int((upper - lower) / 2)
        if boarding_pass[i] == 'L':
            upper -= diff
        else:
            lower += diff
    return lower


print("\n# Part 1")
seat_ids = []
for boarding_pass in input:
    row = get_row(boarding_pass)
    col = get_column(boarding_pass)
    seat_ids.append(row * 8 + col)
print("Highest seat ID: {}".format(max(seat_ids)))

print("\n# Part 2")
seat_ids.sort()
for i, seat_id in enumerate(seat_ids):
    if seat_id + 2 == seat_ids[i + 1]:
        my_seat_id = seat_id + 1
        break
print("My seat ID: {}".format(my_seat_id))
