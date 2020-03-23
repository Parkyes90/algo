def count_ones_by_multiplier(multi):
    dp = [0] * multi
    dp[0] = 1
    idx = 1
    while idx < multi:
        dp[idx] = dp[idx - 1] * 10 + 10 ** idx
        idx += 1
    return dp


def get_multi(n):
    multi = 0
    while n > 1:
        n = n / 10
        if n > 1:
            multi += 1
    return multi


def count_ones(n):
    multiplier = get_multi(n)
    dp = count_ones_by_multiplier(multiplier)
    count = 0
    while n > 10:
        value, n = divmod(n, 10 ** multiplier)
        for i in range(1, value + 1):
            if i == 1:
                count += dp[multiplier - 1] + 10 ** multiplier
            else:
                count += dp[multiplier - 1]
        multiplier -= 1
    if n > 0:
        count += 1
    return count


def dummy_count_ones(n):
    count = 0
    for i in range(1, n + 1):
        count += str(i).count("1")
    return count


if __name__ == "__main__":
    test = 32142342342342343
    count_ones(test)
