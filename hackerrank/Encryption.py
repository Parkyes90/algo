#!/bin/python3

import math

# Complete the encryption function below.
def encryption(s):
    s.replace(" ", "")
    length = len(s)
    cols = math.ceil(math.sqrt(length))
    ret = []
    start = 0
    while start < length:
        ret.append(s[start : start + cols])
        start += cols
    ans = []
    rows = len(ret)
    for c in range(cols):
        tmp = ""
        for r in range(rows):
            try:
                tmp += ret[r][c]
            except IndexError:
                pass
        ans.append(tmp)
    return " ".join(ans)


if __name__ == "__main__":

    result = encryption("haveaniceday")
