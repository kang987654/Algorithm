def dfs(v, g, N):
    visited = [0] * (N+1)
    stack = []

    while True:
        # 목표 지점에 도달 했다면
        if v == g:
            return 1
        # 방문한 적 없는 노드라면
        if visited[v] == 0:
            visited[v] = 1
        # v와 인접한 노드 탐색
        # 방문한 적 없는 인접 노드라면
        # 기존 노드를 스택에 추가하고 기존 노드와 교체
        for w in adj_list[v]:
            if visited[w] == 0:
                stack.append(v)
                v = w
                break
        # 방문한 적 있는 노드라면
        else:
            # 스택에 값이 있다면 다른 노드를 탐색해야하므로
            if stack:
                v = stack.pop()
            # 없다면 목표에 도달할 수 있는 방법이 없음
            else:
                break
    return 0


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    ways = [tuple(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    # 인접 리스트 만들기
    # 행의 인덱스를 노드로 지정 후,
    # 행에 할당된 리스트에는 인접 노드들을 저장
    adj_list = [[] for _ in range(V+1)]
    for s, g in ways:
        adj_list[s].append(g)

    print(f'#{tc} {dfs(S, G, V)}')
