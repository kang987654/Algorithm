for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    hori = []
    cross_1, cross_2 = 0, 0
    vert = [0] * 100
    for i in range(100):
        # 가로는 바로
        hori.append(sum(arr[i]))
        # 대각선
        cross_1 += arr[i][i]    # 역 /
        cross_2 += arr[99-i][i] # /
        # 세로는 따로
        for j in range(100):
            vert[j] += arr[i][j]
            
    print(f'#{tc} {max(max(hori), cross_1, cross_2, max(vert))}')
