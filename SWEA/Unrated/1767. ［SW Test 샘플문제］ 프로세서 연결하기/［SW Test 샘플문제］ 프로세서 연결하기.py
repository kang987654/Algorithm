T = int(input())

dr = [-1, +1, +0, +0]
dc = [+0, +0, -1, +1]


def set_line(r, c, d):
    is_connected, cnt = True, 0

    next_r, next_c = r + dr[d], c + dc[d]
    while 0 <= next_r < N and 0 <= next_c < N:
        # 빈 칸이라면 전선 놓기
        if cpu[next_r][next_c] == 0:
            cnt += 1
            cpu[next_r][next_c] = 2

            next_r += dr[d]
            next_c += dc[d]
        # 전선이 있거나 다른 코어가 있다면 놓던 전선 지우기
        else:
            is_connected, cnt = False, 0
            del_line(next_r, next_c, d)
            break

    return is_connected, cnt


def del_line(r, c, d):
    next_r, next_c = r - dr[d], c - dc[d]

    # 전선만 지우기
    while cpu[next_r][next_c] == 2:
        cpu[next_r][next_c] = 0
        next_r -= dr[d]
        next_c -= dc[d]


def dfs(idx, powered_core, wire):
    global max_core, min_wire

    # 종결 조건
    if idx == len(cores):
        if powered_core > max_core:
            max_core = powered_core
            min_wire = wire
        elif powered_core == max_core:
            min_wire = min(wire, min_wire)
        return

    # 가지치기
    remain = len(cores) - idx
    if powered_core + remain < max_core:
        return

    now_r, now_c = cores[idx]

    for d in range(4):
        is_connected, _len = set_line(now_r, now_c, d)
        dfs(idx+1, powered_core + is_connected, wire + _len)
        # 백트래킹
        if is_connected:
            if d == 0:
                del_line(-1, now_c, d)
            if d == 1:
                del_line(N, now_c, d)
            if d == 2:
                del_line(now_r, -1, d)
            if d == 3:
                del_line(now_r, N, d)


for tc in range(1, T + 1):
    N = int(input())
    cpu = [list(map(int, input().split())) for _ in range(N)]

    cores = []
    # 가장자리는 이미 연결된 코어라 제외
    for i in range(1, N-1):
        for j in range(1, N-1):
            if cpu[i][j] == 1:
                cores.append((i, j))

    max_core = 0
    min_wire = 100

    dfs(0, 0, 0)

    print(f'#{tc} {min_wire}')
