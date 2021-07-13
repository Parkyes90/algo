from typing import List


class Solution:
    def countMatches(
        self, items: List[List[str]], ruleKey: str, ruleValue: str
    ) -> int:
        rule_map = {"type": 0, "color": 1, "name": 2}
        count = 0
        rule_key = rule_map[ruleKey]
        for item in items:
            if item[rule_key] == ruleValue:
                count += 1
        return count


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
