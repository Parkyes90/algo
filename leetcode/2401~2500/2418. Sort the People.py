from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        tuples = []
        for name, height in zip(names, heights):
            tuples.append((name, height))
        print(tuples)
        tuples.sort(key=lambda x: x[1], reverse=True)
        return [t[0] for t in tuples]


if __name__ == "__main__":
    s = Solution()
    answer = s.sortPeople(["Alice", "Bob", "Bob"], [155, 185, 150])
    assert answer == ["Bob", "Alice", "Bob"]
