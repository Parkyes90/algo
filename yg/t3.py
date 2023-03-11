import random


def remove_by_index(start_s: str, s: str, start_index: int):
    is_remove_available = False
    remove_set = {"AB", "BA", "CD", "DC"}
    removed_s = start_s
    for i in range(start_index, len(s), 2):
        target = s[i: i + 2]
        if target not in remove_set:
            removed_s += target
        else:
            is_remove_available = True
    return removed_s, is_remove_available


def remove(s: str):
    removed_s, is_remove_available = remove_by_index("", s, 0)

    if len(removed_s) < 2:
        return removed_s, is_remove_available
    removed_s, is_remove_available = remove_by_index(removed_s[0], removed_s, 1)

    return removed_s, is_remove_available


def solution2(s: str):
    if len(s) < 2:
        return s

    removed_s, is_remove_available = remove(s)
    while is_remove_available and len(removed_s) > 1:
        removed_s, is_remove_available = remove(removed_s)
    return removed_s


def solution(s: str):
    stack = []
    remove_set = {"AB", "BA", "CD", "DC"}
    for item in s:
        if not stack or stack[-1] + item not in remove_set:
            stack.append(item)
        else:
            stack.pop(-1)
    return "".join(stack)


if __name__ == "__main__":
    assert solution("ACBDACBD") == "ACBDACBD"
    assert solution("CABABD") == ""
    assert solution("CBACD") == "C"
    assert solution("AB") == ""
    assert solution("A") == "A"
    assert solution("ACD") == "A"
    assert solution("CDA") == "A"
    assert solution("AC") == "AC"
    assert solution("CA") == "CA"
    assert solution("ABCD") == ""
    test_case = "".join(random.choices("ABCD", k=250000))
    print(solution(test_case))
    print(len(solution(test_case)))
