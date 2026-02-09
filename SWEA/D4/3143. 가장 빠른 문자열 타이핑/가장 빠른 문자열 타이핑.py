T = int(input())

for tc in range(1, T+1):
    A, B = input().split()

    len_a, len_b = len(A), len(B)
    press = 0   # 타이핑 수
    keep = 0    # B로 단축될 동안 안 누르기
    for i in range(len_a):
        # keep > 0 이라면 skip
        if keep:
            keep -= 1
        # A[i:i+len_b] == B 라면 B 한 번 누르고 len_b - 1 만큼 keep
        elif i+len_b <= len_a and A[i:i+len_b] == B:
            press += 1
            keep = len_b - 1
        # 다르다면 타이핑
        else:
            press += 1

    print(f'#{tc} {press}')
