from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for log in logs:
            if log in {"../"}:
                if count:
                    count -= 1
            elif log not in {"./"}:
                count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    answer = s.minOperations(["d1/", "../", "../", "../"])
    print(answer)
