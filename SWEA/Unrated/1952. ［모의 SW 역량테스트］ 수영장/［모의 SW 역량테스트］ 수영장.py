T = int(input())


def set_price(month, price):
    global min_price

    if month > 12:
        min_price = min(price, min_price)
        return

    # 가지치기
    if price > min_price:
        return

    # 0 이면 스킵
    if plan[month] == 0:
        set_price(month+1, price)
    # m3
    set_price(month+3, price+m3)
    # m1
    if plan[month] * d1 > m1:
        set_price(month+1, price+m1)
    # d1
    else:
        set_price(month+1, price+d1*plan[month])


for tc in range(1, T+1):
    d1, m1, m3, y1 = map(int, input().split())
    plan = [0] + list(map(int, input().split()))

    min_price = y1
    set_price(1, 0)

    print(f'#{tc} {min_price}')
