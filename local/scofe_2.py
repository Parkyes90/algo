def solution(a1, a2):
    dp = [1, 1, 2, 3, 5]

    for i in range(5, a1):
        dp.append(dp[i - 2] + dp[i - 1])

    count = 0
    maps = []
    for index, el in enumerate(a2):
        if el == "1":
            count += 1
        else:
            maps.append(count)
            count = 0
        if index == a1 - 1:
            maps.append(count)
    answer = 1
    for m in maps:
        answer *= dp[m - 1]
    return answer


if __name__ == "__main__":
    n = int(input())
    paths = input()
    print(solution(n, paths))
