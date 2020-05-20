from typing import List


class Solution:
    def busyStudent(
        self, startTime: List[int], endTime: List[int], queryTime: int
    ) -> int:
        count = 0
        for start, end in zip(startTime, endTime):
            for i in range(start, end + 1):
                if i == queryTime:
                    count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    answer = s.busyStudent(
        [9, 8, 7, 6, 5, 4, 3, 2, 1], [10, 10, 10, 10, 10, 10, 10, 10, 10], 5
    )
    print(answer)
