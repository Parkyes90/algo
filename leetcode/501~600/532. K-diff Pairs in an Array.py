from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        count_map = {}
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
        count = 0
        for key in count_map:
            if k == 0 and count_map[key] > 1:
                count += 1
            elif k != 0 and key + k in count_map:
                count += 1

        return count


if __name__ == "__main__":
    s = Solution()
    answer = s.findPairs([1, 2, 3, 4, 5], 1)
    print(answer)
