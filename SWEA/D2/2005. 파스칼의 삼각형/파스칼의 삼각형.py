T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 파스칼의 삼각형 만들기
    arr = [[0]*N for _ in range(N)]
    arr[0][0] = 1
    for i in range(1, N):
        arr[i][0] = 1
        for j in range(1, i+1):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    # 역 / 아래부분 출력
    print(f'#{tc}')
    for i in range(N):
        print(*arr[i][:i+1])
