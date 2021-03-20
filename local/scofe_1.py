def solution(a1, a2):
    timestamps = []

    def to_int(x):
        return int(x)

    for t_pair in a2:
        start, end = map(lambda x: x.strip(), t_pair.split("~"))
        start_hour, start_minute = map(to_int, start.split(":"))
        end_hour, end_minute = map(to_int, end.split(":"))
        timestamps.append(
            (
                start_hour * 3600 + start_minute * 60,
                end_hour * 3600 + end_minute * 60,
            )
        )
    max_time = min(map(lambda x: x[1], timestamps))
    min_time = max(map(lambda x: x[0], timestamps))
    if min_time > max_time:
        return -1

    def generate_time_format(t):
        hour, remain = divmod(t, 3600)
        hour = hour if hour > 10 else f"0{hour}"
        minute = remain // 60
        minute = minute if minute > 10 else f"0{minute}"
        return f"{hour}:{minute}"

    return (
        f"{generate_time_format(min_time)} ~ {generate_time_format(max_time)}"
    )


if __name__ == "__main__":
    n = int(input())
    times = []
    for _ in range(n):
        times.append(input())
    print(n, times)
    print(solution(n, times))
