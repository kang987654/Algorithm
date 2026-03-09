T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    bin_m = bin(M)[2:].zfill(N)
    target = bin_m[-N:]
    if '0' in target:
        print(f'#{tc} OFF')
    else:
        print(f'#{tc} ON')
