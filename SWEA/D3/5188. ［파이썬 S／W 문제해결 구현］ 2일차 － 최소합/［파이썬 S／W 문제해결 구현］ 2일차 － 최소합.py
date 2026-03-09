T = int(input())

dr = [+1, +0]
dc = [+0, +1]


def find_way(now_i, now_j, path):
    global min_way

    if now_i == N-1 and now_j == N-1:
        min_way = min(path, min_way)
        return

    # 가지치기
    if path >= min_way:
        return
    
    for di, dj in zip(dr, dc):
        next_i, next_j = now_i + di, now_j + dj
        if next_i < N and next_j < N:
            find_way(next_i, next_j, path+arr[next_i][next_j])


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_way = 250
    find_way(0, 0, arr[0][0])

    print(f'#{tc} {min_way}')
