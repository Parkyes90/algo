from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        sit_seats = (i for i, seat in enumerate(seats) if seat)
        prev, _next = None, next(sit_seats)
        ret = 0
        for i, seat in enumerate(seats):
            if seat:
                prev = i
            else:
                while _next is not None and _next < i:
                    _next = next(sit_seats, None)
                left = float("inf") if prev is None else i - prev
                right = float("inf") if _next is None else _next - i
                ret = max(ret, min(left, right))
        return ret


if __name__ == "__main__":
    s = Solution()
    answer = s.maxDistToClosest([1, 0])
    print(answer)
