def Battle(i, j):
    # 멈추는 조건
    if i == j:
        return i

    # 먼저 구간을 반으로 나누고 각 각 계산 계산
    mid = (i+j)//2
    i = Battle(i, mid)
    j = Battle(mid + 1, j)

    # 승자 반환
    if cards[i] == 1:   # 가위
        if cards[j] == 1:   # 가위
            return i
        if cards[j] == 2:   # 바위
            return j
        if cards[j] == 3:   # 보
            return i
    if cards[i] == 2:   # 바위
        if cards[j] == 1:   # 가위
            return i
        if cards[j] == 2:   # 바위
            return i
        if cards[j] == 3:   # 보
            return j
    if cards[i] == 3:   # 보
        if cards[j] == 1:   # 가위
            return j
        if cards[j] == 2:   # 바위
            return i
        if cards[j] == 3:   # 보
            return i


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = [0] + list(map(int, input().split()))

    print(f'#{tc} {Battle(1, N)}')
