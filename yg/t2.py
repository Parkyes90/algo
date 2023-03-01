import string


def solution(N):
    frequency = (N // len(string.ascii_lowercase)) + 1
    answer = ""
    index = 0
    while len(answer) < N:
        if len(answer) + frequency <= N:
            answer += string.ascii_lowercase[index] * frequency
        else:
            nested_frequency = frequency
            while len(answer) + nested_frequency > N:
                nested_frequency -= 1

            answer += string.ascii_lowercase[index] * nested_frequency
        if index >= len(string.ascii_lowercase) - 1:
            index = 0
        else:
            index += 1

    return answer


if __name__ == "__main__":
    print(solution(10000))
