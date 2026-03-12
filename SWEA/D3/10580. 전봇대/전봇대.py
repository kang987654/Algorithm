T = int(input())

for tc in range(1, T+1):
    N = int(input())
    wire = [list(map(int, input().split())) for _ in range(N)]

    wire.sort(key=lambda w: w[0])
    cnt = 0
    for i in range(len(wire)):
        for j in range(i+1, len(wire)):
            if wire[i][1] > wire[j][1]:
                cnt += 1

    print(f'#{tc} {cnt}')
