import heapq

dr = [-1, +1, +0, +0]
dc = [+0, +0, -1, +1]

def dijkstra():
    recover = [[float('inf')] * N for _ in range(N)]
    recover[0][0] = 0

    hq = [(0, 0, 0)]
    while hq:
        now_recover, r, c = heapq.heappop(hq)

        if now_recover > recover[r][c]:
            continue

        for di, dj in zip(dr, dc):
            next_r, next_c = r + di, c + dj
            if 0 <= next_r < N and 0 <= next_c < N:
                next_recover = now_recover + H[next_r][next_c]
                if next_recover < recover[next_r][next_c]:
                    recover[next_r][next_c] = next_recover
                    heapq.heappush(hq, (next_recover, next_r, next_c))

    return recover[N-1][N-1]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    H = [list(map(int, input())) for _ in range(N)]

    result = dijkstra()

    print(f'#{tc} {result}')
