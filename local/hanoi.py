def hanoi(count, fr, by, to):
    if count < 2:
        return [[fr, to]]

    ret = []

    ret += hanoi(count - 1, fr, to, by)
    ret.append([fr, to])
    ret += hanoi(count - 1, by, fr, to)
    return ret


if __name__ == "__main__":
    print(hanoi(1, 1, 2, 3))
