def find_path(node):
    global cnt

    if node == G:
        cnt += 1
        return
    
    for e in edge[node]:
        if not visited[e]:
            visited[e] = True
            find_path(e)
            visited[e] = False


T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    edges = list(map(int, input().split()))
    S, G = map(int, input().split())

    edge = [[] for _ in range(N+1)]
    for i in range(E):
        edge[edges[2*i]].append(edges[2*i+1])

    visited = [False] * (N+1)
    visited[S] = True
    cnt = 0
    find_path(S)

    print(f'#{tc} {cnt}')
