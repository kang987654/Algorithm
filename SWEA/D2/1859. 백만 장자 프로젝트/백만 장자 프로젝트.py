T = int(input())

for tc in range(1, T+1):
    N = int(input())
    future = list(map(int, input().split()))

    future.reverse()
    max_price = future[0]
    income = 0
    for f in future:
        if f > max_price:
            max_price = f
        else:
            income += max_price - f

    print(f'#{tc} {income}')
