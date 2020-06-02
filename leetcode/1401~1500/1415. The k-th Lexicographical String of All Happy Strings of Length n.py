class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        letters = ["a", "b", "c"]
        ret = []

        def backtrack(string, count):
            if count == n:
                ret.append(string)
                return

            for ch in letters:
                if count > 0:
                    if ch != string[-1]:
                        backtrack(string + ch, count + 1)
                else:
                    backtrack(string + ch, count + 1)

        backtrack("", 0)
        # print(res)
        return "" if (k - 1) >= len(ret) else ret[k - 1]
