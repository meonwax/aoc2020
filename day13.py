import math

with open('day13.txt', 'r') as f:
    input = [line.strip() for line in f.readlines()]

print("\n# Part 1")
earliest_departure = int(input[0])
bus_ids = [int(id) for id in input[1].split(',') if id != 'x']
next_departures = {}
for bus_id in bus_ids:
    next_departures[math.ceil(earliest_departure / bus_id) * bus_id] = bus_id
next_departure = min(next_departures)
print("Result:", (next_departure - earliest_departure) * next_departures[next_departure])
