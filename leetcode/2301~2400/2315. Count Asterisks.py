class Solution:
    def countAsterisks(self, s: str) -> int:
        split = s.split("|")
        count = 0
        for part in split[::2]:
            count += part.count("*")
        return count


if __name__ == "__main__":
    solution = Solution()
    answer = solution.countAsterisks("l|*e*et|c**o|*de|")
    assert answer == 2

    answer = solution.countAsterisks("iamprogrammer")
    assert answer == 0

    answer = solution.countAsterisks("yo|uar|e**|b|e***au|tifu|l")
    assert answer == 5
