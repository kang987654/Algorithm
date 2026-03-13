T = int(input())


def make_top(idx, h):
    global min_h

    # 종결조건
    if h >= B:
        min_h = min(h, min_h)
        return

    # 가지치기
    if h > min_h:
        return

    for i in range(idx, N):
        make_top(i + 1, h + H[i])


for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))

    H.sort(reverse=True)
    min_h = sum(H)
    make_top(0, 0)

    print(f'#{tc} {min_h - B}')
