from typing import List


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        answer = []
        left_sum = 0
        right_sum = sum(nums)

        for num in nums:
            right_sum -= num
            answer.append(abs(left_sum - right_sum))
            left_sum += num
        return answer


if __name__ == "__main__":
    s = Solution()
    assert s.leftRigthDifference([1]) == [0]
