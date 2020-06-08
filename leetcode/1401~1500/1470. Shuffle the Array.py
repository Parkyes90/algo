from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ret = []
        left, right = nums[:n], nums[n:]
        left.reverse()
        right.reverse()
        while left and right:
            ret += [left.pop(), right.pop()]
        return ret


if __name__ == "__main__":
    s = Solution()
    answer = s.shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4)
    print(answer)
