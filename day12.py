with open('day12.txt', 'r') as f:
    input = [line.strip() for line in f.readlines()]

DIRECTION_MAPPING = {
    0: 'N',
    90: 'E',
    180: 'S',
    270: 'W',
}

MOVEMENT_MAPPING = {
    'N': (0, -1),
    'E': (1, 0),
    'S': (0, 1),
    'W': (-1, 0),
}

print("\n# Part 1")
ship_x = 0
ship_y = 0
ship_direction = 90

for instruction in input:
    action = instruction[0]
    value = int(instruction[1:])
    if action == 'F':
        action = DIRECTION_MAPPING[ship_direction]
    if action in MOVEMENT_MAPPING:
        ship_x += MOVEMENT_MAPPING[action][0] * value
        ship_y += MOVEMENT_MAPPING[action][1] * value
    else:
        if action == 'L':
            value = 360 - value
        ship_direction = (ship_direction + value) % 360

print("Manhattan distance:", abs(ship_x) + abs(ship_y))

print("\n# Part 2")
ship_x = 0
ship_y = 0
waypoint_x = 10
waypoint_y = -1

for instruction in input:
    action = instruction[0]
    value = int(instruction[1:])
    if action in MOVEMENT_MAPPING:
        waypoint_x += MOVEMENT_MAPPING[action][0] * value
        waypoint_y += MOVEMENT_MAPPING[action][1] * value
    elif action == 'F':
        ship_x += value * waypoint_x
        ship_y += value * waypoint_y
    else:
        if action == 'L':
            value = 360 - value
        for _ in range(int(value / 90)):
            temp_x = waypoint_x
            waypoint_x = waypoint_y * -1
            waypoint_y = temp_x

print("Manhattan distance:", abs(ship_x) + abs(ship_y))
