def navi(now, dis):
    global min_dis

    if now == N:
        min_dis = min(min_dis, dis)
        return

    if dis > min_dis:
        return

    for e, w in roads[now]:
        navi(e, dis+w)


T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    roads = [[] for _ in range(N)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        roads[s].append((e, w))

    min_dis = float('inf')
    navi(0, 0)

    print(f'#{tc} {min_dis}')
