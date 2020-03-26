from typing import List


class Solution:
    def product(self, nums: List[int]):
        ret = 1
        for n in nums:
            ret *= n
        return ret

    def maximumProduct(self, nums: List[int]) -> int:
        negatives = []
        positives = []
        for n in sorted(nums):
            if n <= 0:
                negatives.append(n)
            else:
                positives.append(n)
        if not positives:
            return self.product(negatives[-3:])
        if not negatives:
            return self.product(positives[-3:])
        if len(positives) == 2:
            return self.product(positives + [negatives[-1]])
        if len(positives) == 1:
            return self.product(positives + negatives[:2])
        if len(negatives) == 1:
            return self.product(positives[-3:])
        if self.product(positives[-3:-1]) < self.product(negatives[:2]):
            return self.product(negatives[:2] + [positives[-1]])
        return self.product(positives[-3:])


if __name__ == "__main__":
    s = Solution()
    answer = s.maximumProduct([1, 2, 3, 4])
    assert answer == 24
    answer = s.maximumProduct([0, -1, -2, -3, -4])
    assert answer == 0
    answer = s.maximumProduct([0, -1, -2, -3, -4, 10, 2, 3])
    assert answer == 120
    answer = s.maximumProduct(
        [
            722,
            634,
            -504,
            -379,
            163,
            -613,
            -842,
            -578,
            750,
            951,
            -158,
            30,
            -238,
            -392,
            -487,
            -797,
            -157,
            -374,
            999,
            -5,
            -521,
            -879,
            -858,
            382,
            626,
            803,
            -347,
            903,
            -205,
            57,
            -342,
            186,
            -736,
            17,
            83,
            726,
            -960,
            343,
            -984,
            937,
            -758,
            -122,
            577,
            -595,
            -544,
            -559,
            903,
            -183,
            192,
            825,
            368,
            -674,
            57,
            -959,
            884,
            29,
            -681,
            -339,
            582,
            969,
            -95,
            -455,
            -275,
            205,
            -548,
            79,
            258,
            35,
            233,
            203,
            20,
            -936,
            878,
            -868,
            -458,
            -882,
            867,
            -664,
            -892,
            -687,
            322,
            844,
            -745,
            447,
            -909,
            -586,
            69,
            -88,
            88,
            445,
            -553,
            -666,
            130,
            -640,
            -918,
            -7,
            -420,
            -368,
            250,
            -786,
        ]
    )
    assert answer == 943695360
