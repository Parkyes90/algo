from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        exclude = set()
        for index, letter in enumerate(s):
            if letter in exclude:
                continue

            distance_index = ord(letter) - 97
            letter_distance = distance[distance_index]
            try:
                if letter != s[index + letter_distance + 1]:
                    return False
            except IndexError:
                return False
            exclude.add(letter)
        return True


if __name__ == "__main__":
    assert (
        Solution().checkDistances(
            "abaccb",
            [
                1,
                3,
                0,
                5,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
        )
        is True
    )
    assert (
        Solution().checkDistances(
            "aa",
            [
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
        )
        is False
    )
