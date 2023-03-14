class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        coordinates_map = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7,
            "8": 0,
            "7": 1,
            "6": 2,
            "5": 3,
            "4": 4,
            "3": 5,
            "2": 6,
            "1": 7,
        }

        chessboard = [
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
        ]

        return (
            chessboard[coordinates_map[coordinates[1]]][coordinates_map[coordinates[0]]]
            == 1
        )


if __name__ == "__main__":
    s = Solution()
    assert s.squareIsWhite("a1") is False
    assert s.squareIsWhite("h3") is True
