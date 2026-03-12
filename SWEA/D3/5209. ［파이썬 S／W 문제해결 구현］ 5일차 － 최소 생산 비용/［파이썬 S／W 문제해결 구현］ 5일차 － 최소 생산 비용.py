T = int(input())


def set_prod(idx, v):
    global min_v

    if idx == N:
        min_v = min(v, min_v)
        return

    if v > min_v:
        return

    for j in range(N):
        if not visited[j]:
            visited[j] = True
            set_prod(idx+1, v + V[idx][j])
            visited[j] = False


for tc in range(1, T+1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]

    min_v = 1500
    visited = [False] * N
    set_prod(0, 0)

    print(f'#{tc} {min_v}')
