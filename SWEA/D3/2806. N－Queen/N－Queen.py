T = int(input())


def can_queen(r, c):
    for i in range(N):
        # 세로
        if board[i][c]:
            return False
        # 가로
        if board[r][i]:
            return False
        # \
        if (0 <= r-i and 0 <= c-i and board[r-i][c-i]) or (r+i < N and c+i < N and board[r+i][c+i]):
            return False
        # 역 \
        if (0 <= r-i and c+i < N and board[r-i][c+i]) or (r+i < N and 0 <= c-i and board[r+i][c-i]):
            return False
    return True


def n_queen(r, n):
    global cnt

    # 종결 조건
    if n == N:
        cnt += 1
        return

    # 가지치기
    if r > n:
        return

    for i in range(r, N):
        for j in range(N):
            if can_queen(i, j):
                board[i][j] = 'Q'
                n_queen(i+1, n+1)
                board[i][j] = ''


for tc in range(1, T+1):
    N = int(input())
    board = [[''] * N for _ in range(N)]

    cnt = 0
    n_queen(0, 0)

    print(f'#{tc} {cnt}')
