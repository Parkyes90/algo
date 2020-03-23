#!/bin/python3

# Complete the organizingContainers function below.
def organizingContainers(container):
    rows = len(container)
    cols = len(container[0])
    cs = []
    rs = []
    for c in range(cols):
        csum = 0
        for r in range(rows):
            csum += container[r][c]
        cs.append(csum)

    for r in range(rows):
        rsum = 0
        for c in range(cols):
            rsum += container[r][c]
        rs.append(rsum)
    cs.sort()
    rs.sort()
    if cs == rs:
        return "Possible"

    return "Impossible"


if __name__ == "__main__":

    containers = [
        [[1, 3, 1], [2, 1, 2], [3, 3, 3]],
        [[0, 2, 1], [1, 1, 1], [2, 0, 0]],
    ]
    for q_itr in range(2):
        result = organizingContainers(containers[q_itr])
