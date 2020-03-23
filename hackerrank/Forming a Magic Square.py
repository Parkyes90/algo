#!/bin/python3

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    min_value = float("inf")
    magic_squares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]
    for magic_square in magic_squares:
        total = 0
        for i in range(3):
            for j in range(3):
                total += abs(magic_square[i][j] - s[i][j])
        min_value = min(total, min_value)
    return min_value


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = []

    # for _ in range(3):
    #     s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare([[4, 9, 2], [3, 5, 7], [8, 1, 5]])

    # fptr.write(str(result) + '\n')

    # fptr.close()
