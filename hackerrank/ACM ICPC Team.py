#!/bin/python3


# Complete the acmTeam function below.
def acmTeam(topic):
    row = len(topic)
    knows = []
    for i in range(row):
        for j in range(i + 1, row):
            count = 0
            for a, b in zip(topic[i], topic[j]):
                if a == "1" or b == "1":
                    count += 1
            knows.append(count)
    maximum = max(knows)
    return [maximum, knows.count(maximum)]


if __name__ == "__main__":
    result = acmTeam(
        [
            ["1", "0", "1", "0", "1"],
            ["1", "1", "1", "0", "0"],
            ["1", "1", "0", "1", "0"],
            ["0", "0", "1", "0", "1"],
        ]
    )
