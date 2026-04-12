import heapq

dr = [-1, +1, +0, +0]
dc = [+0, +0, -1, +1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]

    fuels = [[float('inf')] * N for _ in range(N)]
    fuels[0][0] = 0
    stack = [(0, 0, 0)]
    while stack:
        f, r, c = heapq.heappop(stack)

        if f > fuels[r][c]:
            continue

        fuels[r][c] = f

        for di, dj in zip(dr, dc):
            next_r, next_c = r + di, c + dj
            if 0 <= next_r < N and 0 <= next_c < N:
                if H[r][c] < H[next_r][next_c]:
                    next_f = f + 1 + H[next_r][next_c] - H[r][c]
                else:
                    next_f = f + 1

                if next_f < fuels[next_r][next_c]:
                    fuels[next_r][next_c] = next_f
                    heapq.heappush(stack, (next_f, next_r, next_c))

    print(f'#{tc} {fuels[N-1][N-1]}')
