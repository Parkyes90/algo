def solution(a1, a2, a3):
    counts = []
    minimum = min(a3)
    minimum_index = a3.index(minimum)
    available_ranges = []
    for i in range(a2):
        start_index = minimum_index - i
        end_index = start_index + a2 - 1
        if minimum_index - i >= 0 and end_index < a1:
            available_ranges.append((minimum_index - i, end_index))
    for r in available_ranges:
        count = 1
        left, right = r
        left_value, left_remain = divmod(left, a2 - 1)
        count += left_value
        if left_remain:
            count += 1
        right_value, right_remain = divmod(a1 - right - 1, a2 - 1)
        count += right_value
        if right_remain:
            count += 1
        counts.append(count)
    return min(counts)


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solution(n, k, arr))
