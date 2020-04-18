# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


def guess(num: int) -> int:
    if num < 6:
        return 1
    if num > 6:
        return -1
    return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            if guess(mid) == -1:
                right = mid - 1
            elif guess(mid) == 1:
                left = mid + 1
            else:
                return mid
        return -1


if __name__ == "__main__":
    s = Solution()
    answer = s.guessNumber(10)
    print(answer)
