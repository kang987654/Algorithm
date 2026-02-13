T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    nodes = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    visited = [False] * (V+1)
    distance = [0] * (V+1)
    adj_list = [[] for _ in range(V+1)]
    for v, w in nodes:
        adj_list[v].append(w)
        adj_list[w].append(v)

    link = [S]
    visited[S] = True
    while link:
        now = link.pop(0)

        if now == G:
            break

        for w in adj_list[now]:
            if not visited[w]:
                visited[w] = True
                distance[w] = distance[now] + 1
                link.append(w)

    print(f'#{tc} {distance[G]}')
