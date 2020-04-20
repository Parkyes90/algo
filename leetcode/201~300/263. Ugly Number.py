class Solution:
    def isUgly(self, num: int) -> bool:
        if num < 1:
            return False
        prime_factors = {2, 3, 5}
        while num != 1:
            is_divided = False
            for factor in prime_factors:
                if num % factor == 0:
                    is_divided = True
                    num = num // factor
                    break
            if not is_divided:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    answer = s.isUgly(-8)
    print(answer)
