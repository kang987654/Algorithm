def rec(n, m):
    if m == 1:
        return n
    return n * rec(n, m-1)

for _ in range(10):
    tc = int(input())
    N, M = map(int, input().split())
    
    answer = rec(N, M)
    print(f'#{tc} {answer}')
