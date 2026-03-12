T = int(input())

dr = [-1, +1, +0, +0]
dc = [+0, +0, -1, +1]


def break_block(r, c, board_play):
    # 블럭 부수기
    stack = [(r, c)]
    while stack:
        now_r, now_c = stack.pop()

        v = board_play[now_r][now_c]
        board_play[now_r][now_c] = 0

        for di, dj in zip(dr, dc):
            for i in range(1, v):
                next_r = now_r + i*di
                next_c = now_c + i*dj
                if 0 <= next_r < H and 0 <= next_c < W and board_play[next_r][next_c] != 0:
                    stack.append((next_r, next_c))
    # 블럭 내리기
    for j in range(W):
        for i in range(H-1, -1, -1):
            if board_play[i][j] != 0:
                now_i, next_i = i, i+1
                while next_i < H and board_play[next_i][j] == 0:
                    board_play[now_i][j], board_play[next_i][j] = board_play[next_i][j], board_play[now_i][j]
                    now_i = next_i
                    next_i += 1

    return board_play


def play(n, board_now):
    global min_block

    # 종결 조건1: 블럭 남음
    if n == N:
        cnt = 0
        for i in range(H):
            for j in range(W):
                if board_now[i][j] != 0:
                    cnt += 1
        min_block = min(cnt, min_block)
        return

    # 종결 조건2: clear
    if sum(map(sum, board_now)) == 0:
        min_block = 0
        return

    # 왼쪽부터 하나씩 부수기
    for c in range(W):
        for r in range(H):
            if board_now[r][c] != 0:
                board_next = break_block(r, c, [row[:] for row in board_now])
                play(n+1, board_next)
                break


for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]

    min_block = W * H
    play(0, [row[:] for row in board])

    print(f'#{tc} {min_block}')
