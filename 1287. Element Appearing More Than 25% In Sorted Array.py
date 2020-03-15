from typing import List, Union


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> Union[int, None]:
        count_map = {}
        arr_length = len(arr)
        for a in arr:
            if a not in count_map:
                count_map[a] = 1
            else:
                count_map[a] += 1
            if count_map[a] / arr_length > 0.25:
                return a
        return None


if __name__ == "__main__":
    s = Solution()
    answer = s.findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10])
    print(answer)
