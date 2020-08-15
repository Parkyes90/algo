class Solution:
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split(" ")
        month_map = {
            "Jan": "01",
            "Feb": "02",
            "Mar": "03",
            "Apr": "04",
            "May": "05",
            "Jun": "06",
            "Jul": "07",
            "Aug": "08",
            "Sep": "09",
            "Oct": 10,
            "Nov": 11,
            "Dec": 12,
        }
        return (
            f"{year}"
            f"-{month_map[month]}"
            f"-{day[:-2] if len(day[:-2]) > 1 else f'0{day[:-2]}'}"
        )


if __name__ == "__main__":
    s = Solution()
    answer = s.reformatDate("1st Jan 2052")
    print(answer)
