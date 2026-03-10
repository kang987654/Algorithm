T = int(input())

for tc in range(1, T+1):
    N = int(input())
    reqs = [tuple(map(int, input().split())) for _ in range(N)]

    # 작업 시간이 짧은 순으로 앞시간부터
    sort_by_len = sorted(reqs, key=lambda req: (req[1]-req[0], req[0]))
    truck = 0
    day = [False] * 24
    for s, e in sort_by_len:
        # 해당 시간에 작업이 없다면
        if sum(day[s:e]) == 0:
            truck += 1
            for i in range(s, e):
                day[i] = True

    print(f'#{tc} {truck}')
