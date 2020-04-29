from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        if x1 == x2 == x3 or y1 == y2 == y3:
            return False
        points_set = set()

        for i in range(len(points)):
            points_set.add(tuple(points[i]))

        if len(points_set) < 3:
            return False
        try:
            inclination = (y2 - y1) / (x2 - x1)
        except ZeroDivisionError:
            return True
        x_intercept = inclination * x1
        y_intercept = y1
        for i in range(len(points)):
            x, y = points[i]
            y_value = x * inclination - x_intercept + y_intercept
            if y_value != y:
                return True
        return False

    def isBoomerang2(self, points: List[List[int]]) -> bool:

        # x1, y1 = points[0]
        # x2, y2 = points[1]
        # x3, y3 = points[2]

        # if any two of them are identical, then three points are co-linear
        # if three points are co-linear, then reject

        # the triangle area enclosed by three points is zero if and only if three points are co-linear.
        determinant = (points[0][0] - points[1][0]) * (
            points[1][1] - points[2][1]
        ) - (points[0][1] - points[1][1]) * (points[1][0] - points[2][0])

        if determinant == 0:
            return False

        return True


if __name__ == "__main__":
    s = Solution()
    answer = s.isBoomerang([[0, 2], [0, 2], [2, 0]])
    print(answer)
