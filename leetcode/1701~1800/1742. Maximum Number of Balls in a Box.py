from collections import defaultdict


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = defaultdict(int)
        for i in range(lowLimit, highLimit + 1):
            target_box = 0
            for digit in str(i):
                target_box += int(digit)
            boxes[target_box] += 1
        return max(boxes.values())


if __name__ == "__main__":
    s = Solution()
    assert s.countBalls(1, 10) == 2
    assert s.countBalls(5, 15) == 2
    assert s.countBalls(19, 28) == 2
