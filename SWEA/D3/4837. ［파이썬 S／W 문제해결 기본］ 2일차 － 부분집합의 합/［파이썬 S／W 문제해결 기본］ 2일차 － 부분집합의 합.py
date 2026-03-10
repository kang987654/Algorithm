T = int(input())


def sub_sum(n, idx, _sum):
    global cnt

    if n == N:
        if _sum == K:
            cnt += 1
        return

    if _sum >= K:
        return

    for i in range(idx, 12):
        sub_sum(n+1, i+1, _sum+A[i])


for tc in range(1, T+1):
    N, K = map(int, input().split())

    A = list(range(1, 13))
    cnt = 0
    sub_sum(0, 0, 0)

    print(f'#{tc} {cnt}')
