def dijkstra(graph, start, end):
    # 거리 기록
    distance = {}
    # 지나간 길 기록
    cache = {}
    # graph hash table
    graph_map = {}
    # 정점 목록
    vertices = set()
    # graph hash table 이용한 자료구조화
    for edge in graph:
        start_vertex, end_vertex, weight = edge
        if start_vertex not in graph_map:
            graph_map[start_vertex] = {end_vertex: weight}
        else:
            graph_map[start_vertex][end_vertex] = weight
        if end_vertex not in graph_map:
            graph_map[end_vertex] = {start_vertex: weight}
        else:
            graph_map[end_vertex][start_vertex] = weight
        # 정점 리스트
        vertices.add(start_vertex)
    # 각 정점들 간의 거리 초기화
    for vertex in vertices:
        distance[vertex] = float("inf")
        cache[vertex] = None
    # 시작점 초기화
    distance[start] = 0
    current = start
    while graph_map:
        # 현재 남아있는 정점과 기록된 최소 거리를 이용하여 다음 탐색할 정점 선택
        keys = graph_map.keys()
        minimum = float("inf")
        for key in keys:
            if minimum > distance[key]:
                minimum = distance[key]
                current = key
        # 목적지 정점에 도착할 경우 종료
        if current == end:
            break
        # 이미 지나간 정점 삭제
        del graph_map[current]
        # 인접 정점 목록
        edges = {}
        for edge in graph_map:
            if current in graph_map[edge]:
                edges[edge] = graph_map[edge]
        # 최소 거리 갱신
        # 지나간 길 기록
        for edge in edges:
            if distance[edge] > distance[current] + edges[edge][current]:
                distance[edge] = distance[current] + edges[edge][current]
                cache[edge] = current
    full_path = []
    while current:
        full_path.append(current)
        current = cache[current]
    return list(reversed(full_path)), distance[end]


if __name__ == "__main__":
    g = [
        ("a", "b", 4),
        ("b", "d", 5),
        ("b", "c", 2),
        ("c", "a", 3),
        ("d", "f", 5),
        ("d", "c", 3),
        ("d", "e", 1),
        ("e", "c", 6),
        ("f", "z", 7),
        ("f", "g", 2),
        ("g", "e", 5),
        ("z", "g", 4),
    ]
    s = "a"
    e = "z"
    path_list, shortest_distance = dijkstra(g, s, e)
    print(path_list, shortest_distance)
