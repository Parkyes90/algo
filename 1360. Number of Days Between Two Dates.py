class Solution:
    def is_leaf_year(self, year):
        if year % 400 == 0:
            return True

        if year % 100 == 0:
            return False

        if year % 4 == 0:
            return True

    def get_month_map(self, year):
        return {
            1: 31,
            2: 29 if self.is_leaf_year(year) else 28,
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

    def daysBetweenDates(self, date1: str, date2: str) -> int:
        year1, month1, day1 = map(lambda x: int(x), date1.split("-"))
        year2, month2, day2 = map(lambda x: int(x), date2.split("-"))

        date1_days = day1
        date2_days = day2
        for year in range(1970, year1):
            date1_days += 366 if self.is_leaf_year(year) else 365
        for year in range(1970, year2):
            date2_days += 366 if self.is_leaf_year(year) else 365
        for month in range(1, month1):
            date1_days += self.get_month_map(year1)[month]
        for month in range(1, month2):
            date2_days += self.get_month_map(year2)[month]
        return abs(date2_days - date1_days)


if __name__ == "__main__":
    s = Solution()
    answer = s.daysBetweenDates("2020-01-15", "2019-12-31")
    print(answer)
