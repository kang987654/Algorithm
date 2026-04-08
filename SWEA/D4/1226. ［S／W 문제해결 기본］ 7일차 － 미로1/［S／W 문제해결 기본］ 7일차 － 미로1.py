dr = [-1, +1, +0, +0]
dc = [+0, +0, -1, +1]


def able_miro(s, e):
    next_way = [(s[0], s[1])]
    miro[s[0]][s[1]] = 1

    while next_way:
        r, c = next_way.pop()

        if (r, c) == e:
            return 1
        
        for di, dj in zip(dr, dc):
            next_r, next_c = r + di, c + dj
            if 0 <= next_r < N and 0 <= next_c < N and miro[next_r][next_c] != 1:
                miro[next_r][next_c] = 1
                next_way.append((next_r, next_c))
    
    return 0


for _ in range(10):
    tc = int(input())
    N = 16
    miro = [list(map(int, input())) for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                start = (i, j)
            if miro[i][j] == 3:
                end = (i, j)

    print(f'#{tc} {able_miro(start, end)}' )
