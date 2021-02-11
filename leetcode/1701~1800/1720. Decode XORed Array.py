from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first, *(None for _ in range(len(encoded)))]
        for i in range(len(encoded)):
            # encoded[i] = origin[i] ^ origin[i+1]
            # origin[i+1] = origin[i]
            ans[i + 1] = ans[i] ^ encoded[i]
        return ans


if __name__ == "__main__":
    s = Solution()
    answer = s.decode([1, 2, 3], 1)
    assert answer == [1, 0, 2, 1]
