from collections import deque

def make_n_to_m(N):
    queue = deque([(N, 0)])
    visited = [False] * 1000001
    visited[N] = True

    while queue:
        t, c = queue.popleft()

        if t == M:
            return c
        
        for nt in (t*2, t+1, t-1, t-10):
            if 1 <= nt <= 1000000 and not visited[nt]:
                visited[nt] = True
                queue.append((nt, c+1))

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    cnt = make_n_to_m(N)

    print(f'#{tc} {cnt}')
