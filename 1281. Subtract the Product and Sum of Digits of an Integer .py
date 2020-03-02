class Solution:
    """https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/"""

    def subtractProductAndSum(self, n: int) -> int:
        pd = 1
        sm = 0
        for el in str(n):
            num_el = int(el)
            pd *= num_el
            sm += num_el
        return pd - sm


if __name__ == "__main__":
    s = Solution()
    result = s.subtractProductAndSum(4421)
    print(result)
