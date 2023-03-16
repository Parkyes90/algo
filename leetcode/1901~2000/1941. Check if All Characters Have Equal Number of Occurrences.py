from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        if len(s) == 1:
            return True

        counter = Counter(s)

        values = list(counter.values())

        for i in range(1, len(values)):
            prev, current = values[i - 1], values[i]

            if prev != current:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.areOccurrencesEqual("abacbc") is True
    assert s.areOccurrencesEqual("aaabb") is False
