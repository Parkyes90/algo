class Solution:
    def numberOfMatches(self, n: int) -> int:
        teams = n
        matches = 0
        while teams > 1:
            value, remain = divmod(teams, 2)
            teams = value + remain
            matches += value
        return matches


if __name__ == "__main__":
    s = Solution()
    answer = s.numberOfMatches(14)
    assert 13 == answer
