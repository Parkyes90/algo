from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        value = 0
        for o in operations:
            if "--" in o:
                value -= 1
            else:
                value += 1
        return value


if __name__ == "__main__":
    s = Solution()
    ans = s.finalValueAfterOperations(["--X", "X++", "X++"])
    print(ans)
