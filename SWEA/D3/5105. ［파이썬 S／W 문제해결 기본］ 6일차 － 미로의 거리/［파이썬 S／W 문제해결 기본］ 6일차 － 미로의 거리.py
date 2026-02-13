T = int(input())

for tc in range(1, T+1):
    N = int(input())
    miro = [list(input()) for _ in range(N)]

    si, sj = None, None
    ei, ej = None, None
    for i in range(N):
        for j in range(N):
            if miro[i][j] == '2':
                si, sj = i, j
            if miro[i][j] == '3':
                ei, ej = i, j

    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * N for _ in range(N)]
    distance = [[0] * N for _ in range(N)]

    visited[si][sj] = True
    player = [(si, sj)]
    while player:
        ni, nj = player.pop(0)

        if miro[ni][nj] == '3':
            distance[ni][nj] -= 1
            break

        for di, dj in move:
            if 0 <= ni + di < N and 0 <= nj + dj < N and \
               miro[ni+di][nj+dj] != '1' and not visited[ni+di][nj+dj]:
                visited[ni+di][nj+dj] = True
                distance[ni + di][nj + dj] = distance[ni][nj] + 1
                player.append((ni+di, nj+dj))

    print(f'#{tc} {distance[ei][ej]}')
