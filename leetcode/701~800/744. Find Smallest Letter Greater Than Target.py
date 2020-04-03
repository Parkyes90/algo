from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        bigger = []
        smaller = []
        for letter in letters:
            if target < letter:
                bigger.append(letter)
            elif target > letter:
                smaller.append(letter)

        if bigger:
            return min(bigger)

        return min(smaller)


if __name__ == "__main__":
    s = Solution()
    answer = s.nextGreatestLetter(["c", "f", "j"], "k")
    print(answer)
