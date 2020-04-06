from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        ret = []
        sub_sum = 0
        total_sum = sum(nums)
        for n in nums:
            ret.append(n)
            sub_sum += n
            total_sum -= n
            if sub_sum > total_sum:
                break
        return ret


if __name__ == "__main__":
    s = Solution()
    answer = s.minSubsequence([6])
    print(answer)
