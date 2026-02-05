T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 초기값 세팅
    arr = [[0]*N for _ in range(N)]
    x, y = 0, 0

    # 숫자 넣기 시작
    num = 1
    arr[x][y] = num
    while num < N*N:
        # right
        while y+1 < N and arr[x][y+1] == 0:
            num += 1
            y += 1
            arr[x][y] = num
        # down
        while x+1 < N and arr[x+1][y] == 0:
            num += 1
            x += 1
            arr[x][y] = num
        # left
        while 0 <= y-1 and arr[x][y-1] == 0:
            num += 1
            y -= 1
            arr[x][y] = num
        # up
        while 0 <= x-1 and arr[x-1][y] == 0:
            num += 1
            x -= 1
            arr[x][y] = num

    print(f'#{tc}')
    for row in arr:
        print(*row)