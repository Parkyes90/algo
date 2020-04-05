class Solution:
    def countLargestGroup(self, n: int) -> int:
        count_map = {}
        maximum = 0
        for i in range(1, n + 1):
            digits_sum = 0
            for el in str(i):
                digits_sum += int(el)
            if digits_sum not in count_map:
                count_map[digits_sum] = 1
            else:
                count_map[digits_sum] += 1
            if count_map[digits_sum] > maximum:
                maximum = count_map[digits_sum]
        return len(list(filter(lambda x: x == maximum, count_map.values())))


if __name__ == "__main__":
    s = Solution()
    answer = s.countLargestGroup(10000)
    print(answer)
