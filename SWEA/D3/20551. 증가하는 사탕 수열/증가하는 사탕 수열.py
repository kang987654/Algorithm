T = int(input())

for tc in range(1, T+1):
    A, B, C = map(int, input().split())

    eat = 0
    if C <= B:
        # B - eat = C - 1
        eat += B - (C - 1)
        B = C-1
    if B <= A:
        # A - eat = B - 1
        eat += A - (B - 1)
        A = B-1
    if A < 1:
        eat = -1

    print(f'#{tc} {eat}')
