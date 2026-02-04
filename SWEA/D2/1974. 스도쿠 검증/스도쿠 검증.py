def make_box(x, y):
    box = []
    for i in range(3):
        for j in range(3):
            box.append(arr[x+i][y+j])
    return box

T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    valid = 1
    for i in range(9):
        # 가로
        r = arr[i]

        # 세로 만들면서, 작은 격자도
        c = []
        for j in range(9):
            c.append(arr[j][i])

            # 작은 격자 구성
            if i % 3 == 0 and j % 3 == 0:
                b = make_box(i, j)
                
                # 작은 격자 검증
                if len(set(b)) != 9:
                    valid = 0
                    break

        # 가로 세로 검증
        if len(set(r)) != 9 or len(set(c)) != 9:
            valid = 0
            break

    print(f'#{tc} {valid}')