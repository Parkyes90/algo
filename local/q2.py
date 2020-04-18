def go_forward(direction, r, c, rows, office):
    if direction == "north":
        coordinate = r - 1, c
    elif direction == "south":
        coordinate = r + 1, c
    elif direction == "east":
        coordinate = r, c + 1
    else:
        coordinate = r, c - 1
    for element in coordinate:
        if element < 0 or element > rows - 1:
            return r, c
    row, col = coordinate
    if office[row][col] == -1:
        return r, c
    return coordinate


def solution(office, r, c, move):
    answer = 0
    coordinate = (r, c)
    rows = len(office)
    rotate_count = 0
    direction_map = {0: "north", 1: "east", 2: "south", 3: "west"}
    answer += office[r][c] if office[r][c] > -1 else 0
    office[r][c] = 0
    for m in move:
        direction = direction_map[rotate_count % 4]
        row, col = coordinate
        if m == "go":
            coordinate = go_forward(direction, row, col, rows, office)
            row, col = coordinate
            answer += office[row][col]
            office[row][col] = 0
        elif m == "right":
            rotate_count += 1
        else:
            rotate_count -= 1
    return answer


if __name__ == "__main__":
    s = solution(
        [[5, -1, 4], [6, 3, -1], [2, -1, 1]],
        1,
        0,
        ["go", "go", "right", "go", "right", "go", "left", "go"],
    )
    print(s)
