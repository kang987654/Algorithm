def kill_flies(x, y):
    global M
    kill = 0
    for i in range(M):
        for j in range(M):
            kill += arr[x+i][y+j]

    return kill

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    kills = []
    for i in range(N-M + 1):
        for j in range(N-M + 1):
            kills.append(kill_flies(i, j))
    
    print(f'#{tc} {max(kills)}')
