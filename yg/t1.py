def solution(A):
    prev, diff = -1, float("inf")
    for a in sorted(A):
        if prev != -1:
            diff = min(diff, abs(a - prev))
        prev = a
    return diff


if __name__ == "__main__":
    assert solution([7, 13, 10, 5]) == 2
    assert solution([7, 13, 10, 5, 4]) == 1
    assert solution([12313, 23, 32, 31, 32]) == 0
