class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        _map = {}
        for idx, letter in enumerate(s):
            if letter not in _map:
                _map[letter] = [idx]
            else:
                _map[letter].append(idx)
        maximum = -1
        for value in _map.values():
            if len(value) > 1:
                diff = max(value) - min(value) - 1
                if diff > maximum:
                    maximum = diff
        return maximum


if __name__ == "__main__":
    s = Solution()
    answer = s.maxLengthBetweenEqualCharacters("aa")
    print(answer)
