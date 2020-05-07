from typing import List


def filter_dir_list(dir_list: List[str]) -> List[str]:
    du = [d for d in dir_list]
    for i in range(len(dir_list)):
        for j in range(len(dir_list)):
            if i == j:
                continue
            if dir_list[i] in dir_list[j]:
                du[j] = None
    return [d for d in du if d is not None]


if __name__ == "__main__":
    # ? "c/a/b/c?
    test_dir_list = ["a/b/c", "a/b", "a/b/c/d", "a/b/g", "a/e/j", "a/e/j/n"]
    answer = filter_dir_list(test_dir_list)
    print(answer)
