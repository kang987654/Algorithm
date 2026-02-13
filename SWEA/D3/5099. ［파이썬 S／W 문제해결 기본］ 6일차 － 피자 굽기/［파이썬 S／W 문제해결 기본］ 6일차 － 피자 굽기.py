T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))

    pizzas = [[i+1, Ci[i]] for i in range(M)]
    oven = [pizzas.pop(0) for _ in range(N)]
    while len(oven) > 1:
        idx, cheese = oven.pop(0)
        cheese = cheese//2
        # 치즈가 다 녹았다면
        if cheese == 0:
            # 남은 피자가 있으면 넣고
            if pizzas:
                idx, cheese = pizzas.pop(0)
            # 없으면 오븐에서 돌리기
            elif oven:
                continue
        oven.append([idx, cheese])

    print(f'#{tc} {oven[0][0]}')
