HALF_INDICATORS = {
    'F': 0,
    'B': 1,
    'L': 0,
    'R': 1
}

with open('day05.txt', 'r') as f:
    input = [line.strip() for line in f.readlines()]


def halve_interval(interval, half_indicator):
    half = int(len(interval) / 2)
    if half_indicator == 0:
        return interval[:half]
    if half_indicator == 1:
        return interval[half:]


print("\n# Part 1")
seat_ids = []
for boarding_pass in input:
    row_interval = [i for i in range(0, 128)]
    cols_interval = [i for i in range(0, 8)]
    for char in boarding_pass[:7]:
        row_interval = halve_interval(row_interval, HALF_INDICATORS[char])
    for char in boarding_pass[7:]:
        cols_interval = halve_interval(cols_interval, HALF_INDICATORS[char])
    seat_ids.append(row_interval[0] * 8 + cols_interval[0])
print("Highest seat ID: {}".format(max(seat_ids)))

print("\n# Part 2")
for seat_id in seat_ids:
    if (seat_id + 2 in seat_ids) and not (seat_id + 1 in seat_ids):
        my_seat_id = seat_id + 1
        break
print("My seat ID: {}".format(my_seat_id))
