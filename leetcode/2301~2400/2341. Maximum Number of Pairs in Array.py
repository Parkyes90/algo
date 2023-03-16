from typing import List
from collections import Counter


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        answer = [0, 0]

        for key, value in counter.items():
            answer[0] += value // 2
            if value % 2 == 1:
                answer[1] += 1
        return answer


if __name__ == "__main__":
    s = Solution()
    assert s.numberOfPairs([1, 3, 2, 1, 3, 2, 2]) == [3, 1]
    assert s.numberOfPairs([1, 1]) == [1, 0]
    assert s.numberOfPairs([0]) == [0, 1]
