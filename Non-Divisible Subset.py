#!/bin/python3

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#


def nonDivisibleSubset(k, s):
    """https://www.hackerrank.com/challenges/non-divisible-subset/problem"""

    count_map = [0] * k
    for el in s:
        count_map[el % k] += 1
    total = min(count_map[0], 1)
    for i in range(1, k // 2 + 1):
        if i != k - i:
            total += max(count_map[i], count_map[k - i])
    if k % 2 == 0:
        total += 1
    return total


if __name__ == "__main__":
    fptr = open("test_case.txt", "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + "\n")

    fptr.close()
