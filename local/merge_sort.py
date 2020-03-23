from typing import List


def merge(left: List[int], right: List[int]) -> List[int]:
    """
    stable 한 (기존 원본 배열의 순서를 보장할 수 있음.)
    최악 시간 복잡도: n * Log n
    """
    ret = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] >= right[right_index]:
            ret.append(right[right_index])
            right_index += 1
        else:
            ret.append(left[left_index])
            left_index += 1
    if left_index < len(left):
        while left_index < len(left):
            ret.append(left[left_index])
            left_index += 1
    if right_index < len(right):
        while right_index < len(right):
            ret.append(right[right_index])
            right_index += 1
    return ret


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


if __name__ == "__main__":
    unsorted_arr = [10, 4, 2, 3, 9, 12, 34]
    assert merge_sort(unsorted_arr) == sorted(unsorted_arr)
