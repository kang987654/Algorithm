T = int(input())

for tc in range(1, T+1):
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    C = [int(input().strip()) for _ in range(P)]

    cnt = [0] * 5001
    for a, b in AB:
        for i in range(a, b+1):
            cnt[i] += 1

    print(f'#{tc}', end=' ')
    for c in C:
        print(cnt[c], end=' ')
    print()
