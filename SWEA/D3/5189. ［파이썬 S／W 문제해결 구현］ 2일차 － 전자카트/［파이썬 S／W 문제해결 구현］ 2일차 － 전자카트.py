from itertools import permutations

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 가능한 모든 경우의 수 구하기
    ways = []
    for comb in permutations(range(1, N), N-1):
        ways.append([0] + list(comb) + [0])

    # 최소 경로 탐색
    min_way = 1100
    for way in ways:
        this_way = 0
        for i in range(N):
            this_way += arr[way[i]][way[i+1]]
        min_way = min(this_way, min_way)

    print(f'#{tc} {min_way}')
