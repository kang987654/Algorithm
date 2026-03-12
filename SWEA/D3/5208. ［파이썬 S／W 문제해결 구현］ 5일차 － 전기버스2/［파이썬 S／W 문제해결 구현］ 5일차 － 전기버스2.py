T = int(input())

for tc in range(1, T+1):
    tmp = list(map(int, input().split()))
    N, stops = tmp[0], tmp[1:]

    cnt = [100] * N
    cnt[0] = 0
    for i in range(N-1):
        for j in range(1, stops[i]+1):
            if i+j < N:
                cnt[i+j] = min(cnt[i+j], cnt[i]+1)

    print(f'#{tc} {cnt[N-1]-1}')
