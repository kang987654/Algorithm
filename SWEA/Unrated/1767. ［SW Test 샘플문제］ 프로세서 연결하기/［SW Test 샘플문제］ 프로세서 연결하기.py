dr = [-1, +1, +0, +0]
dc = [+0, +0, -1, +1]


def set_line(r, c, d):
    powered, lines = True, 0
    next_r, next_c = r + dr[d], c + dc[d]
    while 0 <= next_r < N and 0 <= next_c < N:
        if cell[next_r][next_c] == 0:
            cell[next_r][next_c] = 2
            lines += 1
            next_r += dr[d]
            next_c += dc[d]
        else:
            del_line(next_r, next_c, d)
            powered, lines = False, 0
            break

    return powered, lines


def del_line(r, c, d):
    next_r, next_c = r - dr[d], c - dc[d]
    while 0 <= next_r < N and 0 <= next_c < N and cell[next_r][next_c] == 2:
        cell[next_r][next_c] = 0
        next_r -= dr[d]
        next_c -= dc[d]


def mexynos(i, powered_core, linked_line):
    global max_core, min_len

    if i == len(cores):
        if powered_core > max_core:
            max_core = powered_core
            min_len = linked_line
        if powered_core == max_core:
            min_len = min(min_len, linked_line)
        return

    if powered_core + (len(cores) - i) < max_core:
        return

    r, c = cores[i]

    mexynos(i+1, powered_core, linked_line)
    for d in range(4):
        powered, add_line = set_line(r, c, d)
        if powered:
            mexynos(i+1, powered_core+powered, linked_line+add_line)
            if d == 0:  del_line(-1,  c, d)
            if d == 1:  del_line( N,  c, d)
            if d == 2:  del_line( r, -1, d)
            if d == 3:  del_line( r,  N, d)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cell = [list(map(int, input().split())) for _ in range(N)]

    cores = []
    for i in range(1, N-1):
        for j in range(1, N-1):
            if cell[i][j] == 1:
                cores.append((i, j))

    max_core = 0
    min_len = float('inf')
    mexynos(0, 0, 0)

    print(f'#{tc} {min_len}')
