T = int(input())


def bin_search(b):
    left, right = 0, len(A)-1
    d = 0

    while left <= right:
        p = (left + right) // 2
        if A[p] == b:
            return True
        if A[p] < b:
            if d == 1:
                return False
            left = p + 1
            d = 1
        if A[p] > b:
            if d == -1:
                return False
            right = p - 1
            d = -1
    return False


for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    find = 0
    for b in B:
        find += bin_search(b)

    print(f'#{tc} {find}')
