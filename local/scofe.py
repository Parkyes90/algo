def solution(a1, a2, a3):
    count = 0
    total_remain = 0
    minimum = min(a3)
    minimum_index = a3.index(minimum)
    offsets = sorted([minimum_index + 1, a1 - minimum_index])
    first_cover_length, second_cover_length = offsets

    def sum_count(length, divider):
        nonlocal count, total_remain
        value, r = divmod(length, divider)
        count += value
        total_remain += r
        if r:
            count += 1

    if first_cover_length <= a2:
        remain = a2 - first_cover_length
        second_cover_length -= remain
        count += 1
    else:
        sum_count(first_cover_length - 1, a2 - 1)
    sum_count(second_cover_length - 1, a2 - 1)
    if total_remain >= a2 - 1:
        count -= 1
    return count


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solution(n, k, arr))
