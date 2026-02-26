import sys
import copy

N = int(sys.stdin.readline())
board_origin = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

#      상, 하, 좌, 우
dr = [-1, +1, +0, +0]
dc = [+0, +0, -1, +1]


def move(board_play, d):
    merged = [[False] * N for _ in range(N)]
    this_range = range(N)
    if d == 1 or d == 3:
        this_range = range(N+1, -1, -1)

    for r in this_range:
        for c in this_range:
            now_r, now_c = r, c
            next_r, next_c = r + dr[d], c + dc[d]
            while 0 <= next_r < N and 0 <= next_c < N:
                if board_play[next_r][next_c] == 0:
                    # 이동하는 방향의 값과 서로 변경
                    board_play[now_r][now_c], board_play[next_r][next_c] = board_play[next_r][next_c], board_play[now_r][now_c]

                    now_r, now_c = next_r, next_c
                    next_r, next_c = next_r + dr[d], next_c + dc[d]
                elif board_play[now_r][now_c] == board_play[next_r][next_c] and (not merged[next_r][next_c]):
                    board_play[now_r][now_c] = 0
                    board_play[next_r][next_c] *= 2

                    merged[next_r][next_c] = True
                    break
                else:
                    break

    return board_play


def get_max(board, n):
    if n == 5:
        max_list.append(max(map(max, board)))
        return

    for direction in range(4):
        get_max(move(copy.deepcopy(board), direction), n+1)


max_list = []
get_max(board_origin, 0)
print(max(max_list))
