from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        maximum = max(salary)
        minimum = min(salary)
        return (sum(salary) - maximum - minimum) / (len(salary) - 2)


if __name__ == "__main__":
    s = Solution()
    answer = s.average([8000, 9000, 2000, 3000, 6000, 1000])
    print(answer)
