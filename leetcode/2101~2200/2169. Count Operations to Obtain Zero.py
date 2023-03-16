class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        while num1 != 0 and num2 != 0:
            if num2 >= num1:
                num2 = num2 - num1
            else:
                num1 = num1 - num2
            count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    assert s.countOperations(2, 3) == 3
    assert s.countOperations(10, 10) == 1
