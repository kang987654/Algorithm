import heapq

dr = [-1, +1, +0, +0]
dc = [+0, +0, -1, +1]

def dijkstra():
    fuel = [[float('inf')] * N for _ in range(N)]
    fuel[0][0] = 0

    hq = [(0, 0, 0)]

    while hq:
        now_fuel, r, c = heapq.heappop(hq)

        if fuel[r][c] < now_fuel:
            continue

        for di, dj in zip(dr, dc):
            next_r, next_c = r + di, c + dj
            if 0 <= next_r < N and 0 <= next_c < N:
                if H[r][c] < H[next_r][next_c]:
                    next_fuel = now_fuel + 1 + H[next_r][next_c] - H[r][c]
                else:
                    next_fuel = now_fuel + 1

                if next_fuel < fuel[next_r][next_c]:
                    fuel[next_r][next_c] = next_fuel
                    heapq.heappush(hq, (next_fuel, next_r, next_c))

    return fuel[N-1][N-1]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]

    result = dijkstra()

    print(f'#{tc} {result}')
