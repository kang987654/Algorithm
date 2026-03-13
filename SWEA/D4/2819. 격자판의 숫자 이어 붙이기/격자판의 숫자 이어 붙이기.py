T = int(input())

dr = [-1, +1, +0, +0]
dc = [+0, +0, -1, +1]


def make_num(_len, now_r, now_c, num):
    if _len == 7:
        nums.add(num)
        return

    num += grid[now_r][now_c]

    for di, dj in zip(dr, dc):
        if 0 <= now_r+di < N and 0 <= now_c+dj < N:
            make_num(_len+1, now_r+di, now_c+dj, num)


for tc in range(1, T+1):
    N = 4
    grid = [list(input().split()) for _ in range(N)]

    nums = set()
    for i in range(N):
        for j in range(N):
            make_num(0, i, j, '')

    print(f'#{tc} {len(nums)}')
