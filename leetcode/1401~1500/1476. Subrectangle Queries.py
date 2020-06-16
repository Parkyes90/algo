from typing import List


class SubrectangleQueries:
    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = [[col for col in row] for row in rectangle]

    def updateSubrectangle(
        self, row1: int, col1: int, row2: int, col2: int, newValue: int
    ) -> None:
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                self.rectangle[row][col] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
if __name__ == "__main__":
    s = SubrectangleQueries([[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]])
    print(s.rectangle)
    s.getValue(0, 2)
    s.getValue(3, 1)

    s.updateSubrectangle(0, 0, 3, 2, 5)
    print(s.rectangle)
    s.getValue(3, 1)
    s.getValue(0, 2)
    s.updateSubrectangle(3, 0, 3, 2, 10)
    print(s.rectangle)
