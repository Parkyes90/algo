from itertools import combinations


def is_under_k(nums, K):
    for i in range(1, len(nums)):
        diff = abs(nums[i - 1] - nums[i])
        if diff > K:
            return False
    return True


def solution(numbers, K):
    length = len(numbers)
    if is_under_k(numbers, K):
        return 0
    index_list = (i for i in range(length))
    swap_combs = list(combinations(index_list, 2))
    for i in range(1, length):
        combs = combinations(swap_combs, i)
        for comb in combs:
            temp = [n for n in numbers]
            for x, y in comb:
                temp[x], temp[y] = temp[y], temp[x]
            if is_under_k(temp, K):
                return i
    return -1


def count_iter(n):
    count = 0
    index_list = (i for i in range(n))
    swap_combs = list(combinations(index_list, 2))
    for i in range(n):
        combs = combinations(swap_combs, i)
        for comb in combs:
            for _, _ in comb:
                count += 1
    multiplier = 0
    while count:
        count //= n
        multiplier += 1
    return multiplier


if __name__ == "__main__":
    # ans = solution([3], 3)
    # print(ans)
    c = count_iter(8)
    print(c)
