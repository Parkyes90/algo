from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        length = len(s)
        shuffle = ["" for _ in range(length)]
        for i, idx in enumerate(indices):
            shuffle[idx] = s[i]
        return "".join(shuffle)


if __name__ == "__main__":
    s = Solution()
    answer = s.restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3])
    print(answer)
