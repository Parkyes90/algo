def solution(p, s):
    answer = 0
    for i, j in zip(p, s):
        int_i, int_j = int(i), int(j)
        diff = abs(int_i - int_j)
        if diff > 5:
            diff = 10 - diff
        answer += diff
    return answer


if __name__ == "__main__":
    ans = solution("00000000000000000000", "91919191919191919191")
    print(ans)
