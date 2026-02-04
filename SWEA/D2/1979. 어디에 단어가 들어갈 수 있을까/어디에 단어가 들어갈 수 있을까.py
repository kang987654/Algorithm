T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 가능한 단어 길이 모음
    rows, cols = [], []
    for i in range(N):
        kr, kc = 0, 0
        for j in range(N):
            # 가로 길이들
            if arr[i][j] == 0:
                rows.append(kr)
                kr = 0
            else:
                kr += 1
            
            # 세로 길이들
            if arr[j][i] == 0:
                cols.append(kc)
                kc = 0
            else:
                kc += 1

        rows.append(kr)
        cols.append(kc)

    print(f'#{tc} {rows.count(K) + cols.count(K)}')