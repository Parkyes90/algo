import math


def equation(x):
    return x - normal(x) / diff(x)


def normal(x):
    return math.sin(x) + x - 1 / 2


def diff(x):
    return math.cos(x) + 1


if __name__ == "__main__":
    an = 0
    for _ in range(20):
        an = equation(an)
        print(an)
    print(an)
