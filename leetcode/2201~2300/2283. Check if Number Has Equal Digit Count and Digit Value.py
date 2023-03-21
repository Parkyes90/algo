from collections import defaultdict


class Solution:
    def digitCount(self, num: str) -> bool:
        counter1 = defaultdict(int)
        counter2 = defaultdict(int)
        for i, digit in enumerate(num):
            counter1[i] += int(digit)
            counter2[int(digit)] += 1

        for k, v in counter1.items():
            if counter2[k] != v:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.digitCount("1210") is True
    assert s.digitCount("030") is False
