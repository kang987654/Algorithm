##### Prim #####
import heapq

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]

    graph = [[] for _ in range(V+1)]
    for a, b, weight in edges:
        graph[a].append((weight, b))
        graph[b].append((weight, a))
    
    visited = [False] * (V+1)
    hq = [(0, 1)]
    result = 0

    while hq:
        weight, node = heapq.heappop(hq)

        if visited[node]:
            continue
        
        visited[node] = True
        result += weight

        for next_weight, next_node in graph[node]:
            if not visited[next_node]:
                heapq.heappush(hq, (next_weight, next_node))


    print(f'#{tc} {result}')


# ##### Krusakal #####
# def find(x):
#     if parent[x] != x:
#         parent[x] = find(parent[x])

#     return parent[x]


# def union(a, b):
#     parent_a = find(a)
#     parent_b = find(b)

#     if parent_a != parent_b:
#         parent[parent_b] = parent_a


# T = int(input())

# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     edges = [list(map(int, input().split())) for _ in range(E)]

#     parent = list(range(V+1))
#     result = 0
#     for a, b, weight in sorted(edges, key=lambda edge: edge[2]):
#         if find(a) != find(b):
#             union(a, b)
#             result += weight

#     print(f'#{tc} {result}')
