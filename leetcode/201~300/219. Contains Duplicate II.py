from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        length = len(nums)
        count_map = {}
        for i in range(length):
            if nums[i] not in count_map:
                count_map[nums[i]] = [i]
            else:
                count_map[nums[i]].append(i)
        for values in count_map.values():
            values_length = len(values)
            for i in range(1, values_length):
                before = values[i - 1]
                current = values[i]
                if current - before <= k:
                    return True
        return False


if __name__ == "__main__":
    s = Solution()
    answer = s.containsNearbyDuplicate([97, 97], 2)
    print(answer)
