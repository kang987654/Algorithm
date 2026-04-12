from collections import deque

dr = [-1, +1, +0, +0]
dc = [+0, +0, -1, +1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    miro = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if miro[i][j] == '2':
                start = (i, j)
            if miro[i][j] == '3':
                end = (i, j)
    
    dist = [[0] * N for _ in range(N)]
    stack = deque([start])
    while stack:
        r, c = stack.popleft()

        if (r, c) == end:
            break

        for di, dj in zip(dr, dc):
            next_r, next_c = r + di, c + dj
            if 0 <= next_r < N and 0 <= next_c < N and \
            dist[next_r][next_c] == 0 and miro[next_r][next_c] != '1':
                dist[next_r][next_c] = dist[r][c] + 1
                stack.append((next_r, next_c))
    
    print(f'#{tc} {dist[end[0]][end[1]] - 1 if dist[end[0]][end[1]] else dist[end[0]][end[1]]}')
