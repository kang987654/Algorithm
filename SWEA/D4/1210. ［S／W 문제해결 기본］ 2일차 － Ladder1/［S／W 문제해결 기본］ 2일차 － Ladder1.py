for _ in range(10):
    tc = int(input())
    origin = [list(map(int, input().split())) for _ in range(100)]

    # 사다리 뒤집기
    reversed_ladder = origin[::-1]
    # 도착점이 시작점
    x = reversed_ladder[0].index(2)

    # 역으로 출발
    for r in range(1, 100):
        line_change = False     # 왼쪽 갔다가 오른쪽으로 다시 돌아감 방지
        # 좌
        while 0 <= x-1 and reversed_ladder[r][x-1]:
            line_change = True
            x -= 1
        # 우
        while x+1 < 100 and not line_change and reversed_ladder[r][x+1]:
            x += 1

    print(f'#{tc} {x}')
