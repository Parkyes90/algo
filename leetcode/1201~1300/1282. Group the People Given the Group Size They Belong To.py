from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        count_map = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] not in count_map:
                count_map[groupSizes[i]] = [i]
            else:
                count_map[groupSizes[i]].append(i)
        ret = []
        for key, value in count_map.items():
            index = 0
            while index < len(value):
                ret.append(value[index : index + key])
                index += key
        return ret


if __name__ == "__main__":
    s = Solution()
    answer = s.groupThePeople([2, 1, 3, 3, 3, 2])
    print(answer)
