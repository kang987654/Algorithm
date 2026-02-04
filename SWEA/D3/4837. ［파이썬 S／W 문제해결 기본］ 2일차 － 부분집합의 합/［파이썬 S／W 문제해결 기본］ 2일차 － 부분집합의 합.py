T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    # 1~12
    origin = list(range(1, 13))
    # 부분 집합의 합을 저장할 리스트
    sub_sum = []
    for i in range(1 << 12):
        sub = []    # 부분 집합
        cnt = 0     # 부분 집합의 원소 수
        for j in range(12):
            if i & (1 << j):
                sub.append(origin[j])
                cnt += 1
        if cnt == N:
            sub_sum.append(sum(sub))

    print(f'#{tc} {sub_sum.count(K)}')