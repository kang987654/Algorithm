T = int(input())

dr = [-1, +1, +0, +0]
dc = [+0, +0, -1, +1]


def fill_room(now_i, now_j, now_num):
    is_connected = True
    while is_connected:
        is_connected = False
        for di, dj in zip(dr, dc):
            next_i, next_j = now_i + di, now_j + dj
            if 0 <= next_i < N and 0 <= next_j < N and A[next_i][next_j] == now_num-1:
                is_connected = True
                cnt[next_i][next_j] = cnt[now_i][now_j] + 1
                now_i, now_j = next_i, next_j
        now_num -= 1

    return now_num


for tc in range(1, T+1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    cnt = [[0] * N for _ in range(N)]
    num = N ** 2
    while num:
        r, c = 0, 0
        for i in range(N):
            for j in range(N):
                if A[i][j] == num:
                    cnt[i][j] = 1
                    r, c = i, j
        num = fill_room(r, c, num)

    max_cnt, min_num = 0, N**2
    for i in range(N):
        for j in range(N):
            if cnt[i][j] > max_cnt:
                max_cnt = cnt[i][j]
                min_num = A[i][j]
            if cnt[i][j] == max_cnt:
                min_num = min(A[i][j], min_num)

    print(f'#{tc} {min_num} {max_cnt}')
