class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        count_map = {}
        b_count_map = {}
        for i in range(len(A)):
            count_map[A[i]] = count_map.get(A[i], 0) + 1
            b_count_map[B[i]] = b_count_map.get(B[i], 0) + 1
        if A == B:
            duplicate_count = 0
            for value in count_map.values():
                if value > 1:
                    duplicate_count += 1
                if duplicate_count > 0:
                    return True
            return False
        else:
            for key in count_map:
                if key not in b_count_map:
                    return False
                if count_map[key] != b_count_map[key]:
                    return False
            diffs = []
            for i in range(len(A)):
                if A[i] != B[i]:
                    diffs.append((A[i], B[i]))
            if len(diffs) > 2:
                return False
            return True


if __name__ == "__main__":
    s = Solution()
    answer = s.buddyStrings("aba", "baa")
    print(answer)
