from typing import List
from itertools import combinations


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        hours = [8, 4, 2, 1]
        minutes = [32, 16, 8, 4, 2, 1]
        indexes = [i for i in range(len(hours) + len(minutes))]
        times = set()
        combs = combinations(indexes, num)
        for comb in combs:
            hour = 0
            minute = 0
            for index in comb:
                if index < 4:
                    hour += hours[index]
                else:
                    minute += minutes[index - 4]
            if hour > 11 or minute > 59:
                continue
            times.add(f"{hour}:{minute if minute > 9 else '0' + str(minute)}")
        return list(times)


if __name__ == "__main__":
    s = Solution()
    answer = s.readBinaryWatch(2)
    print(answer)
