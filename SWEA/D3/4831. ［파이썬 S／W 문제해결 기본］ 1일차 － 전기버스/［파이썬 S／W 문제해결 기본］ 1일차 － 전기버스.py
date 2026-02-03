T = int(input())
 
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    stations = list(map(int, input().split()))
 
    bus = 0
    cnt = 0
    moves = range(K, 0, -1)
    stops = [False] * (N+1)
    for s in stations:
        stops[s] = True
 
    go = True
    while go and (bus < N):
        go = False
        for move in moves:
            if bus+move >= N or stops[bus+move]:
                go = True
                bus += move
                cnt += 1
                break
 
    if bus >= N:
        print(f'#{tc} {cnt-1}')
    else:
        print(f'#{tc} 0')
