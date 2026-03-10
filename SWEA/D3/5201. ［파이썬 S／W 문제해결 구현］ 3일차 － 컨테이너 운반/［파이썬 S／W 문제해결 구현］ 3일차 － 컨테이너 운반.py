T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    T = list(map(int, input().split()))

    # 무거운 순으로 적재 용량이 큰 트럭부터 운반 가능 여부 확인
    W.sort(reverse=True)
    T.sort(reverse=True)

    answer = 0
    idx_truck = 0

    for w in W:
        # 모든 버스가 운반
        if idx_truck == M:
            break

        if w <= T[idx_truck]:
            answer += w
            idx_truck += 1

    print(f'#{tc} {answer}')
