def solution(a1, a2, a3, a4, a5):
    y_list = []
    o_list = []
    genre_map = {}
    score_map = {
        "A": a1[0],
        "B": a1[1],
        "C": a1[2],
        "D": a1[3],
        "E": a1[4],
    }
    for r in range(a4):
        for c in range(a5):
            genre_map[(r, c)] = a3[r][c]

    for r in range(a4):
        for c in range(a5):
            genre = genre_map[(r, c)]
            score = score_map[genre]
            output = f"{genre} {score} {r} {c}"
            if a2[r][c] == "Y":
                y_list.append(output)
            elif a2[r][c] == "O":
                o_list.append(output)
    y_list.sort(key=lambda x: float(x.split()[1]), reverse=True)
    o_list.sort(key=lambda x: float(x.split()[1]), reverse=True)
    return y_list + o_list


if __name__ == "__main__":
    favorites = list(map(lambda x: float(x), input().split()))
    infos = []
    genres = []
    row, col = map(lambda x: int(x), input().split())
    for _ in range(row):
        infos.append(input())
    for _ in range(row):
        genres.append(input())
    answer = solution(favorites, infos, genres, row, col)
    for a in answer:
        print(a)
