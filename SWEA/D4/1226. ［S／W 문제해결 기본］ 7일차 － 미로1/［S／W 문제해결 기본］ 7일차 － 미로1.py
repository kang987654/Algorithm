for _ in range(10):
    tc = input()
    N = 16
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

    visited[si][sj] = True
    player = [(si, sj)]
    while player:
        ni, nj = player.pop(0)

        if miro[ni][nj] == '3':
            break

        for di, dj in move:
            if 0 <= ni + di < N and 0 <= nj + dj < N and \
               miro[ni+di][nj+dj] != '1' and not visited[ni+di][nj+dj]:
                visited[ni+di][nj+dj] = True
                player.append((ni+di, nj+dj))

    print(f'#{tc} {int(visited[ei][ej])}')
