T = int(input())

for tc in range(1, T+1):
    N = int(input())
    
    white = [[0]*10 for _ in range(10)]
    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                # 이미 보라색
                if white[r][c] == 3:
                    continue
                # 백지거나 다른색이면 칠하기
                if white[r][c] == 0 or white[r][c] != color:
                    white[r][c] += color

    # 보라색 count
    cnt = 0
    for r in range(10):
        for c in range(10):
            if white[r][c] == 3:
                cnt += 1
    print(f'#{tc} {cnt}')

