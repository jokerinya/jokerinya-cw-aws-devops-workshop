def final_direction(init, rotations):
    directions = ["N", "E", "S", "W"]
    direction_index = directions.index(init)
    # index changing
    def rotate(value):
        nonlocal direction_index
        direction_index = direction_index + value
        if direction_index >= len(directions): direction_index = 0
        if direction_index < 0 : direction_index = (len(directions)-1)
    
    # rotate checking
    for i in rotations:
        if i == "L":
            rotate(-1)
        else:
            rotate(1)

    return directions[direction_index]

print(final_direction("N", ["L", "L", "L"]))  # E
print(final_direction("N", ["R", "R", "R", "R"]))  # N
print(final_direction("N", ["R", "L"]))  # N
print(final_direction("N", ["R", "R", "R", "L"]))  # S