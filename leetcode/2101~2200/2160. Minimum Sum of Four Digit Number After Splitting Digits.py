from itertools import permutations


class Solution:
    def _generate_new_num_pairs(self, str_num, perms):
        result = set()
        indexes = {0, 1, 2, 3}
        for perm in perms:
            remain = indexes - set(perm)
            perms2 = permutations(remain)
            new1 = ""
            for i in perm:
                new1 += str_num[i]
            for perm2 in perms2:
                new2 = ""
                for i in perm2:
                    new2 += str_num[i]
                result.add((int(new1), int(new2)))
        return result

    def minimumSum(self, num: int) -> int:
        num_pairs = set()
        indexes = {0, 1, 2, 3}
        str_num = str(num)
        num_pairs |= self._generate_new_num_pairs(str_num, permutations(indexes, 3))
        num_pairs |= self._generate_new_num_pairs(str_num, permutations(indexes, 2))
        min_num_pair = min(num_pairs, key=lambda x: x[0] + x[1])
        return sum(min_num_pair)


if __name__ == "__main__":
    s = Solution()
    assert 39 == s.minimumSum(4512)  # 20 31
