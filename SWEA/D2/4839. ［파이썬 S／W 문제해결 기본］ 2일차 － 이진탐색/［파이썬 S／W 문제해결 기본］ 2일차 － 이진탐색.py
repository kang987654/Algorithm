def binary_search(pages, f):
    l, r = 1, pages
    times = 0       # 시행 횟수
    while l <= r:
        times += 1
        c = int((l+r) / 2)
        if f < c:
            r = c
        elif c < f:
            l = c
        else:
            return times


T = int(input())

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    # 게임 결과 확인
    Ra = binary_search(P, Pa)
    Rb = binary_search(P, Pb)

    if Ra < Rb:
        print(f'#{tc} A')
    elif Ra > Rb:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')
