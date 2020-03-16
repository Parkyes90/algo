class Solution:
    """https://leetcode.com/problems/day-of-the-week/submissions/"""

    def is_leap_year(self, year):
        if year % 400 == 0:
            return True

        if year % 100 == 0:
            return False

        if year % 4 == 0:
            return True

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = (
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
            "Monday",
            "Tuesday",
        )
        month_days_map = {
            1: 31,
            2: 29 if self.is_leap_year(year) else 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31,
        }
        acc_days = 0

        for y in range(1970, year):
            if self.is_leap_year(y):
                acc_days += 366
            else:
                acc_days += 365

        for m in range(1, month):
            acc_days += month_days_map[m]
        acc_days += day
        return days[acc_days % 7]


if __name__ == "__main__":
    s = Solution()
    answer = s.dayOfTheWeek(1, 1, 1970)
    print(answer)
