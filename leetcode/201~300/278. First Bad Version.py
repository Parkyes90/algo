# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    if version > 1702766718:
        return True
    return False


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            elif isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1

        return None


if __name__ == "__main__":
    s = Solution()
    answer = s.firstBadVersion(2126753390)
    print(answer)
