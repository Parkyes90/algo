#!/bin/python3
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            start = mid + 1
        else:
            end = mid - 1
    return start


"""https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem"""
# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    """ return List[int]"""
    ret = []
    scores_set = set(scores)
    distinct_scores = sorted(scores_set, reverse=True)

    for a in alice:
        idx = binary_search(distinct_scores, a)
        ret.append(idx + 1)
    return ret


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")
    #
    # scores_count = int(input())
    #
    # scores = list(map(int, input().rstrip().split()))
    #
    # alice_count = int(input())
    #
    # alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(
        [100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]
    )
    print(result)

    # fptr.write("\n".join(map(str, result)))
    # fptr.write("\n")
    #
    # fptr.close()
