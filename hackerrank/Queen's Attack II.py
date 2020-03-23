#!/bin/python3

import os


def queensAttack(n, k, r_q, c_q, obstacles):
    set_ob = set(map(lambda x: tuple(x), obstacles))
    count = 0
    directions = {
        "left",
        "right",
        "up",
        "down",
        "upLeft",
        "upRight",
        "downLeft",
        "downRight",
    }
    for direction in directions:
        row = r_q
        col = c_q
        if direction == "left":
            while 1 < col:
                col -= 1
                if (row, col) in set_ob:
                    break
                else:
                    count += 1
        elif direction == "right":
            while col < n:
                col += 1
                if (row, col) in set_ob:
                    break
                else:
                    count += 1
        elif direction == "up":
            while row < n:
                row += 1
                if (row, col) in set_ob:
                    break
                else:
                    count += 1
        elif direction == "down":
            while 1 < row:
                row -= 1
                if (row, col) in set_ob:
                    break
                else:
                    count += 1
        elif direction == "upLeft":
            while 1 < col and row < n:
                row += 1
                col -= 1
                if (row, col) in set_ob:
                    break
                else:
                    count += 1
        elif direction == "upRight":
            while col < n and row < n:
                row += 1
                col += 1
                if (row, col) in set_ob:
                    break
                else:
                    count += 1
        elif direction == "downLeft":
            while 1 < col and 1 < row:
                row -= 1
                col -= 1
                if (row, col) in set_ob:
                    break
                else:
                    count += 1
        else:
            while col < n and 1 < row:
                row -= 1
                col += 1
                if (row, col) in set_ob:
                    break
                else:
                    count += 1
    return count


if __name__ == "__main__":
    result = queensAttack(4, 0, 4, 4, [])
