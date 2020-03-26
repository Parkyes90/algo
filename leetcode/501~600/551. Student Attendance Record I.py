class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count("A") > 1:
            return False

        l_count = 0
        for el in s:
            if el == "L":
                l_count += 1
            else:
                l_count = 0
            if l_count > 2:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.checkRecord("PPALLP") is True
    assert s.checkRecord("PPALLL") is False
