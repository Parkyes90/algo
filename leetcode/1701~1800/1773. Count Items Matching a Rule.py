from typing import List


class Solution:
    def countMatches(
        self, items: List[List[str]], ruleKey: str, ruleValue: str
    ) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    answer = s.countMatches(
        [
            ["phone", "blue", "pixel"],
            ["computer", "silver", "lenovo"],
            ["phone", "gold", "iphone"],
        ],
        "color",
        "silver",
    )
    assert answer == 1
