import sys
N, M = map(int, sys.stdin.readline().split())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

#      상  하  좌  우
dr = [-1, +1, +0, +0]
dc = [+0, +0, -1, +1]

answer = 0
max_val = max(map(max, paper))
blocks = []


def dfs(r, c, cnt, sumthing):
    global answer

    # 길이가 4
    if cnt == 4:
        answer = max(answer, sumthing)
        return

    # 가지치기
    if sumthing + (4-cnt) * max_val <= answer:
        return

    # ㅗ 모양
    if cnt == 3:
        for i in range(4):
            next_r, next_c = blocks[1][0] + dr[i], blocks[1][1] + dc[i]
            if 0 <= next_r < N and 0 <= next_c < M and (next_r, next_c) not in blocks:
                blocks.append((next_r, next_c))
                dfs(next_r, next_c, cnt + 1, sumthing + paper[next_r][next_c])
                blocks.pop()

    for i in range(4):
        next_r, next_c = r + dr[i], c + dc[i]
        if 0 <= next_r < N and 0 <= next_c < M and (next_r, next_c) not in blocks:
            blocks.append((next_r, next_c))
            dfs(next_r, next_c, cnt+1, sumthing + paper[next_r][next_c])
            blocks.pop()


for row in range(N):
    for col in range(M):
        blocks.append((row, col))
        dfs(row, col, 1, paper[row][col])
        blocks.pop()

print(answer)
