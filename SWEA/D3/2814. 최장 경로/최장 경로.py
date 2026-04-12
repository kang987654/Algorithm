def find_path(v, _len):
    global max_len

    max_len = max(max_len, _len)

    for w in edges[v]:
        if not visited[w]:
            visited[w] = True
            find_path(w, _len+1)
            visited[w] = False


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    edges = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        edges[x].append(y)
        edges[y].append(x)

    max_len = 1
    for i in range(N+1):
        if edges[i]:
            visited = [False] * (N+1)
            visited[i] = True
            find_path(i, 1)

    print(f'#{tc} {max_len}')
