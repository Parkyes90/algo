from itertools import accumulate
from typing import List
from bisect import bisect_right


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        answer = []
        counter = {}
        _sum = 0
        for i, num in enumerate(nums):
            _sum += num
            counter[i] = _sum

        for query in queries:
            length = 0
            while length < len(nums) and counter[length] <= query:
                length += 1
            answer.append(length)
        return answer

    def answerQueries2(self, nums: List[int], queries: List[int]) -> List[int]:

        nums = list(accumulate(sorted(nums)))
        return [bisect_right(nums, q) for q in queries]


if __name__ == "__main__":
    assert Solution().answerQueries2([4, 5, 2, 1], [3, 10, 21]) == [2, 3, 4]
    assert Solution().answerQueries2([2, 3, 4, 5], [1]) == [0]
    assert Solution().answerQueries2(
        [
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
        ],
        [
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
        ],
    )
