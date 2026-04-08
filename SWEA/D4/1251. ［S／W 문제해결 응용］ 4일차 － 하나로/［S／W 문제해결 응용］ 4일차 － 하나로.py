import heapq

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    islands_x = list(map(int, input().split()))
    islands_y = list(map(int, input().split()))
    E = float(input())

    islands = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            L2 = (islands_x[j]-islands_x[i])**2 + (islands_y[j]-islands_y[i])**2
            islands[i].append((E * L2, j))
            islands[j].append((E * L2, i))

    total_cost = 0

    visited = [False] * N
    hq = [(0, 0)]
    while hq:
        now_cost, island = heapq.heappop(hq)

        if visited[island]:
            continue

        visited[island] = True
        total_cost += now_cost

        for next_cost, land in islands[island]:
            if not visited[land]:
                heapq.heappush(hq, (next_cost, land))

    print(f'#{tc} {int(round(total_cost, 0))}')
