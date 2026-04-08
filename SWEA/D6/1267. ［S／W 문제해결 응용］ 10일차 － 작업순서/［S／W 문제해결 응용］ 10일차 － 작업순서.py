from collections import deque

T = 10

for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))

    edges = [[] for _ in range(V+1)]
    in_degrees = [0] * (V+1)
    for i in range(E):
        edges[arr[2*i]].append(arr[2*i+1])
        in_degrees[arr[2*i+1]] += 1

    que = deque()
    for i in range(1, V+1):
        if in_degrees[i] == 0:
            que.append(i)

    result = []
    while que:
        n = que.popleft()
        result.append(n)

        for next_n in edges[n]:
            in_degrees[next_n] -= 1
            if in_degrees[next_n] == 0:
                que.append(next_n)

    print(f'#{tc}', *result)
