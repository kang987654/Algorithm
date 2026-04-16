dr = [-1, +1, +0, +0]
dc = [+0, +0, -1, +1]

def find_top():
    top = max(map(max, mount))
    tops = []
    for i in range(N):
        for j in range(N):
            if mount[i][j] == top:
                tops.append((i, j))

    return tops


def make_path(_len, r, c):
    global max_path

    max_path = max(_len, max_path)

    for di, dj in zip(dr, dc):
        next_r, next_c = r + di, c + dj
        if 0 <= next_r < N and 0 <= next_c < N and mount[next_r][next_c] < mount[r][c]:
            make_path(_len+1, next_r, next_c)


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    mount = [list(map(int, input().strip().split())) for _ in range(N)]

    origin_tops = find_top()
    max_path = 1
    # 공사 X
    for v, w in origin_tops:
        make_path(1, v, w)
    # 공사 O
    for i in range(N):
        for j in range(N):
            for k in range(1, K+1):
                mount[i][j] -= k    # 공사
                for v, w in origin_tops:
                    make_path(1, v, w)
                mount[i][j] += k    # 원위치

    print(f'#{tc} {max_path}')
