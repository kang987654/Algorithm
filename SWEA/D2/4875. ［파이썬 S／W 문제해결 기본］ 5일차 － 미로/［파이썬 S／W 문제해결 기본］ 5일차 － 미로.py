def dfs(now_i, now_j):
    if visited[now_i][now_j] == 0:
        visited[now_i][now_j] = 1

        for di, dj in zip(dr, dc):
            next_i = now_i + di
            next_j = now_j + dj
            if 0 <= next_i < N and 0 <= next_j < N and miro[next_i][next_j] != '1':
                dfs(next_i, next_j)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    miro = [list(input()) for _ in range(N)]

    # 상하좌우
    dr = [-1, +1, +0, +0]
    dc = [+0, +0, -1, +1]

    visited = [[0] * N for _ in range(N)]
    end_i, end_j = 0, 0
    for i in range(N):
        for j in range(N):
            if miro[i][j] == '2':
                dfs(i, j)
            if miro[i][j] == '3':
                end_i, end_j = i, j

    print(f'#{tc} {visited[end_i][end_j]}')
