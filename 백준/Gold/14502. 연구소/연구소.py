import sys
N, M = map(int, sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

#      상  하  좌  우
dr = [-1, +1, +0, +0]
dc = [+0, +0, -1, +1]

rooms, virus = [], []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            rooms.append((i, j))
        if lab[i][j] == 2:
            virus.append((i, j))
len_r = len(rooms)
min_poisoned = N*M


def spread(min_poisoned):
    visited = [[False] * M for _ in range(N)]
    for rv, cv in virus:
        visited[rv][cv] = True
    poisoned = len(virus)
    stack = [v[:] for v in virus]
    while stack:
        now_r, now_c = stack.pop()

        for di, dj in zip(dr, dc):
            next_r, next_c = now_r + di, now_c + dj
            if 0 <= next_r < N and 0 <= next_c < M and lab[next_r][next_c] != 1 and (not visited[next_r][next_c]):
                visited[next_r][next_c] = True
                poisoned += 1
                if poisoned >= min_poisoned:
                    return min_poisoned
                stack.append((next_r, next_c))

    return poisoned


for w1 in range(len_r-2):
    lab[rooms[w1][0]][rooms[w1][1]] = 1
    for w2 in range(w1+1, len_r-1):
        lab[rooms[w2][0]][rooms[w2][1]] = 1
        for w3 in range(w2+1, len_r):
            lab[rooms[w3][0]][rooms[w3][1]] = 1
            min_poisoned = spread(min_poisoned)
            lab[rooms[w3][0]][rooms[w3][1]] = 0
        lab[rooms[w2][0]][rooms[w2][1]] = 0
    lab[rooms[w1][0]][rooms[w1][1]] = 0

print(len_r - 3 + len(virus) - min_poisoned)
