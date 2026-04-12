dr = [-1, +0, +1, +0]
dc = [+0, +1, +0, -1]

def to_the_goal(r, c, d, act, cut, turned):
    global min_act

    if (r, c) == (er, ec):
        min_act = min(act, min_act)
        return
    
    if act >= min_act:
        return

    # 직진
    next_r, next_c = r + dr[d], c + dc[d]
    if 0 <= next_r < N and 0 <= next_c < N and \
    not visited[next_r][next_c] and park[next_r][next_c] != 'T':
        visited[next_r][next_c] = True
        to_the_goal(next_r, next_c, d, act + 1, cut, False)
        visited[next_r][next_c] = False
    elif 0 <= next_r < N and 0 <= next_c < N and \
    not visited[next_r][next_c] and park[next_r][next_c] == 'T' and cut < K:
        visited[next_r][next_c] = True
        to_the_goal(next_r, next_c, d, act + 1, cut + 1, False)
        visited[next_r][next_c] = False
    # 회전
    if not turned:
        to_the_goal(r, c, (d+4 + 1) % 4, act + 1, cut, True)
        to_the_goal(r, c, (d+4 + 2) % 4, act + 2, cut, True)
        to_the_goal(r, c, (d+4 - 1) % 4, act + 1, cut, True)

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    park = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if park[i][j] == 'X':
                sr, sc = i, j
            if park[i][j] == 'Y':
                er, ec = i, j

    min_act = float('inf')

    visited = [[False] * N for _ in range(N)]
    visited[sr][sc] = True
    to_the_goal(sr, sc, 0, 0, 0, False)

    if min_act == float('inf'):
        min_act = -1
    print(f'#{tc} {min_act}')
