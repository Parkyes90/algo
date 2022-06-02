from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        result = 0
        students.sort()
        seats.sort()
        for student, seat in zip(students, seats):
            result += abs(student - seat)
        return result


if __name__ == "__main__":
    s = Solution()
    assert 4 == s.minMovesToSeat(students=[2, 7, 4], seats=[3, 1, 5])
    assert 7 == s.minMovesToSeat(students=[1, 3, 2, 6], seats=[4, 1, 5, 9])
    assert 4 == s.minMovesToSeat(students=[1, 3, 2, 6], seats=[2, 2, 6, 6])
